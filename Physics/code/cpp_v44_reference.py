# Reference implementation for Causal Phase Program v4.4 (CPP v4.4).
# Implements:
#  - Sections 1-6 baseline algebra, admissible ensemble A(nu, k_max), magnetic
#    precision Pi = m^2 I + L_Theta, symmetric phase continuation and causal-reversal
#    invariance of Pi vs sign-flip of Q_W (Lemma 2.4.1), Benettin Lyapunov spectrum,
#    Kozachenko-Leonenko entropy balance (Theorem 4.3), exact 2x2 Woodbury edge swaps
#    (Prop. 6.2), loop expansion (Prop. 6.3, Corollary 6.3.1), and triadic Schur
#    decomposition (Prop. 6.4).
#  - Proposition 6.5: Cross-boundary Wilson action W_cross = S_interface(0) - S_interface(Theta) >= 0,
#    area-law scaling (slope vs secant on 22x22 lattice), and U(1)/SU(2) ratio.
#  - Section 7: Killing-orthogonal decomposition of su(k+m), Schur-Haar fixed subspace
#    u(1)_inter (+) su(m)_dA, canonical generators Q_orth and Q_v, boundary impedance
#    commutator [K_int, K_ext], and exact zero-covariance subspace Pi_I(ker Pi_bI) (Prop. 7.3).
#  - Section 8: Phase epsilon-admissibility condition (L5) |U_D - 1| = sqrt(2 J_xy) < eps
#    (J_xy < eps^2 / 2, eps < 2 sin(pi / (2(d-1)))) and 2D Landau-Dirichlet collar
#    interpolation with Gauss-Legendre & NumPy 2.x compatible quadrature (Theorem 8.2).
#  - Section 12: Self-test suite (Checks [1]-[19]), multigroup W_cross >= 0 test (Sec. 12.2),
#    area-law & U(1)/SU(2) benchmark (Sec. 12.2), and Metropolis V3/V4 driver (Sec. 12.3).
#
# Normative parent: Physics/Causal_Phase_Program_v4_4.md (v4.4)
# Technical Spec:   Physics/Technical_Specification_v0.4.md (v0.4)
# Canonical logic:  Reasoning/Modified_Brusentsov_Entailment_Logic.md (MBEL V_4)

import argparse
from datetime import datetime
import itertools
import os
import sys
import time

import numpy as np
from scipy.linalg import eigvals, pinv
from scipy.sparse.csgraph import connected_components, shortest_path
from scipy.spatial import cKDTree
from scipy.special import digamma, gammaln

# NumPy 1.x / 2.x compatible trapezoidal integration
_trapezoid = getattr(np, "trapezoid", getattr(np, "trapz", None))

# =====================================================================
# 1. CAUSAL-PHASE ALGEBRA & EDGE DIAMOND PARTICIPATION (Sections 1-2)
# =====================================================================

def is_hasse_irreducible(R):
    """Check strict upper-triangularity and transitive irreducibility of the Hasse matrix R."""
    R = np.asarray(R)
    N = len(R)
    if not np.all(np.tril(R) == 0):
        return False
    paths = np.linalg.inv(np.eye(N) - R) - np.eye(N) - R
    return not np.any((R > 0) & (paths > 0.5))


def causal_phase_invariants(R, Theta):
    """Compute K = R^2, M = W^2, frustration J = (K^2 - |M|^2)/K, and cone-commutator norms."""
    W = R * np.exp(1j * Theta)
    K = R @ R
    M = W @ W
    mask = K > 0
    J = np.zeros(K.shape)
    J[mask] = (K[mask] ** 2 - np.abs(M[mask]) ** 2) / K[mask]
    Dp, Dm = W @ W.conj().T, W.conj().T @ W
    C = Dp @ Dm - Dm @ Dp
    L_raw = float(np.real(np.trace(C.conj().T @ C)))
    L_norm = L_raw / (1.0 + np.linalg.norm(Dp, "fro") ** 2 * np.linalg.norm(Dm, "fro") ** 2)
    return K, M, J, L_raw, L_norm


def diamond_participation(R):
    """Diamond-participation multiplicity d_diamond(x,y) of each Hasse edge (Definition 2.1)."""
    Ri = np.asarray(R, dtype=int)
    K = Ri @ Ri
    Kx = np.maximum(0, K - 1)
    d = Ri * (Kx @ Ri.T) + Ri * (Ri.T @ Kx)
    return d, (Ri == 1) & (d == 0), (Ri == 1) & (d >= 1)


def verify_wilson_identity(R, Theta):
    """Numerical verification of the Wilson identity (Proposition 1.1)."""
    K, _, J, _, _ = causal_phase_invariants(R, Theta)
    err = 0.0
    for x, y in zip(*np.where(K >= 2)):
        zs = np.where((R[x] == 1) & (R[:, y] == 1))[0]
        ph = Theta[x, zs] + Theta[zs, y]
        lhs = 0.5 * np.sum(1.0 - np.cos(ph[:, None] - ph[None, :]))
        err = max(err, abs(lhs - 0.5 * K[x, y] * J[x, y]))
        if K[x, y] == 2:
            err = max(err, abs((1.0 - np.cos(ph[0] - ph[1])) - J[x, y]))
    return float(err)

# =====================================================================
# 2. ADMISSIBLE ENSEMBLE (Section 3.2) AND HYPERCUBE COUNTEREXAMPLE (Prop. 3.5)
# =====================================================================

def admissible(R, nu, kmax):
    """Check the hard constraints (L0)-(L4) of the admissible ensemble A(nu, k_max)."""
    N = len(R)
    if not is_hasse_irreducible(R):
        return False
    K = R @ R
    pairs = np.argwhere(K >= 2)
    covered = np.zeros(N, bool)
    for x, y in pairs:
        covered[x] = covered[y] = True
        covered[(R[x] > 0) & (R[:, y] > 0)] = True
    deg = R.sum(0) + R.sum(1)
    connected = connected_components(R + R.T, directed=False)[0] == 1
    return bool(covered.all() and connected and (deg <= kmax).all() and len(pairs) >= nu * N)


def directed_hypercube(dims):
    """Hasse matrix of the product order on the box dims."""
    coords = list(itertools.product(*[range(n) for n in dims]))
    index = {c: i for i, c in enumerate(coords)}
    R = np.zeros((len(coords), len(coords)), dtype=int)
    for c in coords:
        for ax in range(len(dims)):
            c2 = list(c)
            c2[ax] += 1
            if c2[ax] < dims[ax]:
                R[index[c], index[tuple(c2)]] = 1
    return R, coords


def diamond_density_interior(dims):
    """Count of pairs (x,y) with K_xy = 2 at interior hypercube vertices (Proposition 3.5)."""
    R, coords = directed_hypercube(dims)
    K = R @ R
    interior = [i for i, c in enumerate(coords) if all(c[a] <= dims[a] - 3 for a in range(len(dims)))]
    per_vertex = [int(np.sum(K[i] == 2)) for i in interior]
    return int(K.max()), sorted(set(per_vertex)), is_hasse_irreducible(R)

# =====================================================================
# 3. UNIFIED GAUSSIAN MODEL WITH MAGNETIC LAPLACIAN (Sections 2.4, 3.5)
# =====================================================================

def magnetic_precision(R, Theta, m2=0.5):
    """Magnetic precision matrix Pi = m^2 I + L_Theta, L_Theta = D - W - W^dagger."""
    W = R * np.exp(1j * Theta)
    A = W + W.conj().T
    D = np.diag(np.abs(A).sum(axis=1))
    return m2 * np.eye(len(R)) + D - A


def verify_causal_parity_and_lemma_2_4_1(R, Theta, m2=0.5, beta=1.0):
    """
    Verify Lemma 2.4.1:
      1. Symmetric continuation Theta_sym = Theta + Theta^T makes
         W + W^dagger = A_sym * cos(Theta_sym) + i * S_caus * sin(Theta_sym) exact and Hermitian
         (whereas antisymmetric continuation Theta_anti = Theta - Theta^T fails Hermiticity).
      2. Exact causal-reversal symmetries:
         Pi(R^T, -Theta^T) == Pi(R, Theta) and Pi(R^T, Theta^T) == conj(Pi(R, Theta)),
         so ln det Pi is strictly invariant under causal reversal.
      3. Solenoidal drift flips sign under causal reversal:
         Q_W(R^T, -Theta^T) == -Q_W(R, Theta) and Q_W(R^T, Theta^T) == -conj(Q_W(R, Theta)).
    """
    R = np.asarray(R, dtype=float)
    Theta = np.asarray(Theta, dtype=float) * (R > 0)
    W = R * np.exp(1j * Theta)
    A_sym = R + R.T
    S_caus = R - R.T
    Theta_sym = Theta + Theta.T
    rhs_sym = A_sym * np.cos(Theta_sym) + 1j * S_caus * np.sin(Theta_sym)
    sym_err = float(np.max(np.abs((W + W.conj().T) - rhs_sym)))

    Pi_orig = magnetic_precision(R, Theta, m2=m2)
    Pi_rev_neg = magnetic_precision(R.T, -Theta.T, m2=m2)
    Pi_rev_pos = magnetic_precision(R.T, Theta.T, m2=m2)
    pi_neg_err = float(np.max(np.abs(Pi_orig - Pi_rev_neg)))
    pi_pos_err = float(np.max(np.abs(Pi_orig.conj() - Pi_rev_pos)))
    logdet_rev_err = abs(float(np.linalg.slogdet(Pi_orig)[1]) - float(np.linalg.slogdet(Pi_rev_pos)[1]))

    Q_orig = solenoidal_from_transport(R, Theta, beta=beta)
    Q_rev_neg = solenoidal_from_transport(R.T, -Theta.T, beta=beta)
    q_flip_err = float(np.max(np.abs(Q_orig + Q_rev_neg)))
    return {
        "sym_decomp_err": sym_err,
        "pi_rev_neg_err": pi_neg_err,
        "pi_rev_pos_err": pi_pos_err,
        "logdet_rev_err": float(logdet_rev_err),
        "q_flip_err": q_flip_err,
    }


def screening_and_mediated_covariance(Pi, idx_E, idx_b, idx_I):
    """Check screening |Pi_IE| == 0 and the mediated-covariance formula for Sigma_IE."""
    if len(idx_I) == 0 or len(idx_b) == 0 or len(idx_E) == 0:
        raise ValueError("Triad zones must be non-empty: choose A with non-empty interior I_A and complement E_A.")
    S = np.linalg.inv(Pi)
    blk = lambda a, b: Pi[np.ix_(a, b)]
    screen = float(np.max(np.abs(blk(idx_I, idx_E))))
    formula = (np.linalg.inv(blk(idx_I, idx_I)) @ blk(idx_I, idx_b) @ S[np.ix_(idx_b, idx_b)]
               @ blk(idx_b, idx_E) @ np.linalg.inv(blk(idx_E, idx_E)))
    return screen, float(np.max(np.abs(S[np.ix_(idx_I, idx_E)] - formula)))


def kernel_inclusion_violation(Pi, idx_E, idx_b, idx_I):
    """Norm ||Pi_{E,b} P_ker||_2; zero iff ker Pi_Ib is contained in ker Pi_Eb."""
    if len(idx_I) == 0 or len(idx_b) == 0 or len(idx_E) == 0:
        raise ValueError("Triad zones must be non-empty: choose A with non-empty interior I_A and complement E_A.")
    Pi_Ib = Pi[np.ix_(idx_I, idx_b)]
    Pi_Eb = Pi[np.ix_(idx_E, idx_b)]
    P_ker = np.eye(len(idx_b)) - pinv(Pi_Ib) @ Pi_Ib
    return float(np.linalg.norm(Pi_Eb @ P_ker, 2))


def solenoidal_from_transport(R, Theta, beta=1.0):
    """Anti-Hermitian solenoidal drift Q_W = (beta/2)(W - W^dagger) = i*beta*H_rot."""
    W = R * np.exp(1j * Theta)
    return 0.5 * beta * (W - W.conj().T)


def relaxation_gap(Pi, Gamma, Q):
    """Relaxation spectral gap gamma(Q) = min Re spec((Gamma + Q) Pi)."""
    return float(np.min(np.real(eigvals((Gamma + Q) @ Pi))))

# =====================================================================
# 4. NOISY NONLINEAR MODEL, BENETTIN SPECTRUM, AND ENTROPY BALANCE (Section 4)
# =====================================================================

def transport_hermitian(R, Theta):
    W = R * np.exp(1j * Theta)
    return W + W.conj().T


def G_map(psi, Hm, delta, g):
    """Nonlinear contracting map G(psi) = (1 - delta) psi + g H f(psi)."""
    return (1.0 - delta) * psi + g * (Hm @ (psi / np.sqrt(1.0 + np.abs(psi) ** 2)))


def real_jacobian(psi, Hm, delta, g):
    """Real 2n x 2n Jacobian of G in the (Re psi, Im psi) basis."""
    n = len(psi)
    x, y = psi.real, psi.imag
    s = 1.0 / np.sqrt(1.0 + x * x + y * y)
    Df = np.block([[np.diag(s - s**3 * x * x), np.diag(-s**3 * x * y)],
                   [np.diag(-s**3 * x * y), np.diag(s - s**3 * y * y)]])
    Hr = np.block([[Hm.real, -Hm.imag], [Hm.imag, Hm.real]])
    return (1.0 - delta) * np.eye(2 * n) + g * Hr @ Df


def benettin_spectrum(Hm, delta, g, noise, steps=20000, burn=500, seed=0):
    """Full Lyapunov spectrum of z_{t+1} = G(z_t) + xi_t via the Benettin (QR) method."""
    rng = np.random.default_rng(seed)
    n = Hm.shape[0]
    psi = 0.1 * (rng.normal(size=n) + 1j * rng.normal(size=n))
    Q = np.eye(2 * n)
    acc = np.zeros(2 * n)
    for t in range(steps + burn):
        Jt = real_jacobian(psi, Hm, delta, g)
        Q, Rm = np.linalg.qr(Jt @ Q)
        if t >= burn:
            acc += np.log(np.abs(np.diag(Rm)))
        psi = G_map(psi, Hm, delta, g) + noise * (rng.normal(size=n) + 1j * rng.normal(size=n)) / np.sqrt(2)
    return np.sort(acc / steps)[::-1]


def knn_entropy(X, k=5):
    """Kozachenko-Leonenko differential-entropy estimate (nats) from sample X (N, d)."""
    N, d = X.shape
    r = cKDTree(X).query(X, k=k + 1)[0][:, -1]
    log_cd = (d / 2.0) * np.log(np.pi) - gammaln(d / 2.0 + 1.0)
    return float(digamma(N) - digamma(k) + log_cd + d * np.mean(np.log(r)))


def entropy_balance_check(Hm, delta, g, noise, n_samples=200000, burn=150, seed=1, k=5):
    """Independent estimates of Delta_noise = h(G(Z)+xi) - h(G(Z)) and of -E ln|det DG(Z)| (Theorem 4.3)."""
    rng = np.random.default_rng(seed)
    n = Hm.shape[0]
    Z = 0.1 * (rng.normal(size=(n_samples, n)) + 1j * rng.normal(size=(n_samples, n)))
    for _ in range(burn):
        Z = (1 - delta) * Z + g * (Z / np.sqrt(1 + np.abs(Z) ** 2)) @ Hm.T
        Z = Z + noise * (rng.normal(size=Z.shape) + 1j * rng.normal(size=Z.shape)) / np.sqrt(2)
    Y = (1 - delta) * Z + g * (Z / np.sqrt(1 + np.abs(Z) ** 2)) @ Hm.T
    Y2 = Y + noise * (rng.normal(size=Y.shape) + 1j * rng.normal(size=Y.shape)) / np.sqrt(2)
    real = lambda A: np.hstack([A.real, A.imag])
    sub = rng.choice(n_samples, size=min(n_samples, 100000), replace=False)
    logdet = np.mean([np.linalg.slogdet(real_jacobian(Z[i], Hm, delta, g))[1] for i in sub[:4000]])
    h_Z, h_Y, h_Y2 = knn_entropy(real(Z)[sub], k), knn_entropy(real(Y)[sub], k), knn_entropy(real(Y2)[sub], k)
    return {"h_Z": h_Z, "h_GZ": h_Y, "h_GZ_plus_noise": h_Y2,
            "Delta_noise": h_Y2 - h_Y, "minus_E_logdet": -float(logdet),
            "stationarity_gap": h_Y2 - h_Z}

# =====================================================================
# 5. LOCAL FACTOR RANK, TIME RATIOS, AND SYNCHRONIZATION (Sections 3.3, 5)
# =====================================================================

def interval_local_path_quotient(R, Theta, eps_ker=0.30):
    """Interval-local path factorization inside each interval (x, y) (Definition 3.2)."""
    N = len(R)
    K = R @ R
    K_eff = np.zeros((N, N), dtype=int)
    for x, y in zip(*np.where(K >= 1)):
        zs = np.where((R[x] == 1) & (R[:, y] == 1))[0]
        ph = np.sort((Theta[x, zs] + Theta[zs, y]) % (2 * np.pi))
        if len(ph) == 1:
            K_eff[x, y] = 1
            continue
        gaps = np.diff(np.append(ph, ph[0] + 2 * np.pi))
        K_eff[x, y] = max(1, int(np.sum(gaps > eps_ker)))
    return K_eff


def relative_phase_cycle_ratio(delta_N_A, delta_N_B, tol=1e-15):
    """Ratio R_AB (Definition 5.1); returns np.nan for a vanishing denominator."""
    if abs(delta_N_B) <= tol:
        return np.nan
    return float(delta_N_A / delta_N_B)


def sync_time(R, nodes, eps=1e-12):
    """Synchronization time tau_sync = diameter / lambda_2 (Definition 5.2)."""
    idx = np.array(sorted(nodes), dtype=int)
    A = R[np.ix_(idx, idx)]
    A = A + A.T
    dist = shortest_path(A, directed=False, unweighted=True)
    fin = dist[np.isfinite(dist) & (dist > 0)]
    diam = float(fin.max()) if len(fin) else 1.0
    deg = np.maximum(A.sum(1), eps)
    L = np.eye(len(idx)) - np.diag(deg ** -0.5) @ A @ np.diag(deg ** -0.5)
    lam2 = float(max(eps, np.sort(np.linalg.eigvalsh(L))[1]))
    return diam / lam2

# =====================================================================
# 6. TRIAD AND STRUCTURAL TWINS (Sections 2.2, 3.3)
# =====================================================================

def partition_triad(R, A):
    """Partition of the graph into the triad (I_A, dA, E_A) and boundary capacities (Definition 2.2)."""
    A = set(int(a) for a in A)
    N = len(R)
    E = [x for x in range(N) if x not in A]
    nbrs = lambda x: np.where((R[x] + R[:, x]) > 0)[0]
    bnd = [x for x in sorted(A) if any(y not in A for y in nbrs(x))]
    I = [x for x in sorted(A) if x not in bnd]
    cap_out = int(sum(R[x, y] for x in bnd for y in E))
    cap_in = int(sum(R[y, x] for y in E for x in bnd))
    return I, bnd, E, {"cap_out": cap_out, "cap_in": cap_in}


def structural_twins(R):
    """Classes of structural twin vertices with identical non-empty pasts and futures."""
    groups = {}
    for z in range(len(R)):
        if R[z].sum() + R[:, z].sum() == 0:
            continue
        groups.setdefault((tuple(R[:, z]), tuple(R[z])), []).append(z)
    return [g for g in groups.values() if len(g) > 1]

# =====================================================================
# 7. FIELD BACK-REACTION, WOODBURY, LOOP EXPANSION, SCHUR & W_CROSS (Section 6)
# =====================================================================

def structural_and_joint_cost(R, Theta, a=1.0, b=0.5, g=0.1, p=2.0, eta_field=1.0, m2=0.5, T=1.0):
    """
    Base structural functional F_struct and joint co-evolution functional F_joint (Sec. 6.2).
    At Metropolis temperature T > 0, the effective number of bosonic field components is
    n_bos = eta_field / T >= 0.
    """
    if eta_field < 0:
        raise ValueError("The bosonic back-reaction parameter eta_field must be non-negative.")
    K, _, J, L_raw, _ = causal_phase_invariants(R, Theta)
    F_struct = float(a * np.sum(K[K > 0] ** p) + b * np.sum(J) + g * L_raw)
    if eta_field == 0:
        return F_struct, F_struct, 0.0
    Pi = magnetic_precision(R, Theta, m2=m2)
    logdet_Pi = float(np.linalg.slogdet(Pi)[1])
    return F_struct, float(F_struct + eta_field * logdet_Pi), logdet_Pi


def dipole_vector(N, x, y, theta_xy):
    """Dipole incidence vector (v_e)_u = delta_{ux} - exp(-i*theta_xy)*delta_{uy} (Prop. 6.2)."""
    v = np.zeros(N, dtype=complex)
    v[x] = 1.0
    v[y] = -np.exp(-1j * theta_xy)
    return v


def woodbury_edge_swap_ratio(Pi, e_del, theta_del, e_add, theta_add):
    """Exact 2x2 Woodbury ratio det(Pi') / det(Pi) for replacing edge e_del with e_add (Prop. 6.2)."""
    N = len(Pi)
    Sigma = np.linalg.inv(Pi)
    v_minus = dipole_vector(N, e_del[0], e_del[1], theta_del)
    v_plus = dipole_vector(N, e_add[0], e_add[1], theta_add)
    r_minus = float(np.real(v_minus.conj() @ Sigma @ v_minus))
    r_plus = float(np.real(v_plus.conj() @ Sigma @ v_plus))
    cross = complex(v_minus.conj() @ Sigma @ v_plus)
    ratio_woodbury = (1.0 - r_minus) * (1.0 + r_plus) + abs(cross) ** 2
    return float(ratio_woodbury), r_minus, r_plus, float(abs(cross) ** 2)


def loop_expansion_diagnostics(R, Theta, m2=0.5):
    """Checks for Proposition 6.3: inertia of orders l=1,2,3, triangle-freeness, and the diamagnetic bound."""
    W = R * np.exp(1j * Theta)
    A_theta = W + W.conj().T
    A_zero = (R + R.T).astype(float)
    deg = A_zero.sum(axis=1)
    dm_inv_sqrt = np.diag(1.0 / np.sqrt(m2 + deg))

    T_theta = dm_inv_sqrt @ A_theta @ dm_inv_sqrt
    T_zero = dm_inv_sqrt @ A_zero @ dm_inv_sqrt

    tr1 = float(np.real(np.trace(T_theta)))
    tr2_diff = float(abs(np.real(np.trace(T_theta @ T_theta)) - np.trace(T_zero @ T_zero)))
    tr3_theta = float(abs(np.real(np.trace(T_theta @ T_theta @ T_theta))))
    tr3_zero = float(abs(np.trace(T_zero @ T_zero @ T_zero)))

    Pi_theta = magnetic_precision(R, Theta, m2=m2)
    Pi_zero = magnetic_precision(R, np.zeros_like(Theta), m2=m2)
    logdet_theta = float(np.linalg.slogdet(Pi_theta)[1])
    logdet_zero = float(np.linalg.slogdet(Pi_zero)[1])
    quartic_lead = 0.25 * float(
        np.trace(np.linalg.matrix_power(T_zero, 4))
        - np.real(np.trace(np.linalg.matrix_power(T_theta, 4)))
    )

    return {
        "tr1": tr1,
        "tr2_phase_diff": tr2_diff,
        "tr3_theta": tr3_theta,
        "tr3_zero": tr3_zero,
        "Phi_mag_exact": logdet_theta - logdet_zero,
        "quartic_leading_term": quartic_lead,
    }


def single_pi_plaquette_torus_benchmark(L=30, m2=0.5):
    """
    Verifies Corollary 6.3.1 on an L x L periodic square torus at m^2 = 0.5:
      - Leading l=4 loop formula gives 4 / (m^2 + 4)^4 = 4 / 4.5^4 = 0.009755 (~26.3%).
      - Exact all-orders shift per isolated pi-plaquette (vortex-antivortex pair separated
        by L // 2 along a Z_2 Dirac string) equals 0.0372 (~73.7% comes from l >= 6).
    """
    N = L * L
    idx = lambda x, y: (x % L) * L + (y % L)
    A0 = np.zeros((N, N), dtype=complex)
    for x in range(L):
        for y in range(L):
            u = idx(x, y)
            vx, vy = idx(x + 1, y), idx(x, y + 1)
            A0[u, vx] = A0[vx, u] = 1.0
            A0[u, vy] = A0[vy, u] = 1.0
    A_dirac = A0.copy()
    for x in range(L // 2):
        u, v = idx(x, L // 2), idx(x, L // 2 + 1)
        A_dirac[u, v] = A_dirac[v, u] = -1.0
    Pi0 = (m2 + 4.0) * np.eye(N) - A0
    Pi_d = (m2 + 4.0) * np.eye(N) - A_dirac
    exact_per_plaq = 0.5 * float(np.linalg.slogdet(Pi_d)[1] - np.linalg.slogdet(Pi0)[1])
    l4_term = 4.0 / ((m2 + 4.0) ** 4)
    return {
        "exact_per_pi_plaquette": exact_per_plaq,
        "l4_leading_term": l4_term,
        "l4_fraction": l4_term / exact_per_plaq,
        "higher_loops_fraction": 1.0 - (l4_term / exact_per_plaq),
    }


def triadic_schur_decomposition(Pi, idx_I, idx_b, idx_E):
    """Exact triadic Schur decomposition of ln det Pi and the functional S_interface > 0 (Proposition 6.4)."""
    blk = lambda a, b: Pi[np.ix_(a, b)]
    Pi_I, Pi_b, Pi_E = blk(idx_I, idx_I), blk(idx_b, idx_b), blk(idx_E, idx_E)
    Pi_bI, Pi_Ib = blk(idx_b, idx_I), blk(idx_I, idx_b)
    Pi_bE, Pi_Eb = blk(idx_b, idx_E), blk(idx_E, idx_b)

    K_int = Pi_bI @ np.linalg.inv(Pi_I) @ Pi_Ib
    K_ext = Pi_bE @ np.linalg.inv(Pi_E) @ Pi_Eb
    S_dA = Pi_b - K_int - K_ext
    logdet_total = float(np.linalg.slogdet(Pi)[1])
    logdet_I = float(np.linalg.slogdet(Pi_I)[1]) if len(idx_I) else 0.0
    logdet_E = float(np.linalg.slogdet(Pi_E)[1]) if len(idx_E) else 0.0
    logdet_S = float(np.linalg.slogdet(S_dA)[1]) if len(idx_b) else 0.0
    logdet_b = float(np.linalg.slogdet(Pi_b)[1]) if len(idx_b) else 0.0

    return {
        "logdet_total": logdet_total,
        "schur_sum": logdet_I + logdet_E + logdet_S,
        "decomposition_error": abs(logdet_total - (logdet_I + logdet_E + logdet_S)),
        "S_interface_coupling": logdet_b - logdet_S,
        "K_int": K_int,
        "K_ext": K_ext,
    }


def cross_wilson_action_identity(R, Theta, idx_I, idx_b, idx_E, m2=0.5):
    """
    Verifies Proposition 6.5:
      Phi_mag = W_I + W_E + W_b + W_cross,
      W_cross = S_interface(0) - S_interface(Theta) = -Delta S_interface >= 0.
    """
    Pi_th = magnetic_precision(R, Theta, m2=m2)
    Pi_0 = magnetic_precision(R, np.zeros_like(Theta), m2=m2)
    sch_th = triadic_schur_decomposition(Pi_th, idx_I, idx_b, idx_E)
    sch_0 = triadic_schur_decomposition(Pi_0, idx_I, idx_b, idx_E)

    blk_ld = lambda M, idx: float(np.linalg.slogdet(M[np.ix_(idx, idx)])[1])
    W_I = blk_ld(Pi_th, idx_I) - blk_ld(Pi_0, idx_I)
    W_E = blk_ld(Pi_th, idx_E) - blk_ld(Pi_0, idx_E)
    W_b = blk_ld(Pi_th, idx_b) - blk_ld(Pi_0, idx_b)
    Phi_mag = sch_th["logdet_total"] - sch_0["logdet_total"]

    W_cross = sch_0["S_interface_coupling"] - sch_th["S_interface_coupling"]
    identity_err = abs(Phi_mag - (W_I + W_E + W_b + W_cross))
    return {
        "Phi_mag": Phi_mag,
        "W_cross": W_cross,
        "Delta_S_interface": -W_cross,
        "identity_err": identity_err,
    }

# =====================================================================
# 8. INTER-SCALE U(1) COMMUTANT & L5 CONTINUUM INTERPOLATION (Sections 7-8)
# =====================================================================


def boundary_effective_gap(Pi, Q, idx_b, idx_I, idx_E, Gamma_scale=1.0):
    """
    Schur-reduced boundary dynamics for the pair (Pi, Q_W).
    Returns M_eff = Tr(K_int), full-system gap, boundary gap with/without core,
    and Tr(K_ext).
    """
    blk = lambda a, b: Pi[np.ix_(a, b)]
    Pi_I = blk(idx_I, idx_I)
    Pi_b = blk(idx_b, idx_b)
    Pi_E = blk(idx_E, idx_E)
    Pi_bI, Pi_Ib = blk(idx_b, idx_I), blk(idx_I, idx_b)
    Pi_bE, Pi_Eb = blk(idx_b, idx_E), blk(idx_E, idx_b)

    K_int = Pi_bI @ np.linalg.inv(Pi_I) @ Pi_Ib
    K_ext = Pi_bE @ np.linalg.inv(Pi_E) @ Pi_Eb
    S_dA = Pi_b - K_int - K_ext

    M_eff = float(np.real(np.trace(K_int)))
    tr_ext = float(np.real(np.trace(K_ext)))

    n = Pi.shape[0]
    Gamma = Gamma_scale * np.eye(n)
    g_full = relaxation_gap(Pi, Gamma, Q)

    nb = len(idx_b)
    if nb == 0:
        return {"M_eff": M_eff, "Tr_Kext": tr_ext, "gamma_full": g_full,
                "gamma_bdry": float("nan"), "gamma_bdry0": float("nan"), "d_gamma": float("nan")}

    Qb = Q[np.ix_(idx_b, idx_b)]
    Gb = Gamma_scale * np.eye(nb)
    g_bdry = float(np.min(np.real(eigvals((Gb + Qb) @ S_dA))))
    S0 = Pi_b - K_ext
    g_bdry0 = float(np.min(np.real(eigvals((Gb + Qb) @ S0))))
    return {
        "M_eff": M_eff,
        "Tr_Kext": tr_ext,
        "gamma_full": g_full,
        "gamma_bdry": g_bdry,
        "gamma_bdry0": g_bdry0,
        "d_gamma": g_bdry - g_bdry0,
        "K_int": K_int,
        "S_dA": S_dA,
    }


def schur_boundary_gap_scaling_check(L=12, m2=0.5, beta=1.0, seed=7, verbose=True):
    """
    Numerical check (Sec. 7 / Prop. 6.4 extension):
      - M_eff(A) = Tr K_int(A) grows with core size;
      - K_int shifts the boundary relaxation gap: gamma_bdry < gamma_bdry0 (d_gamma < 0);
      - |d_gamma| decreases with increasing m^2 (stronger screening).
    """
    rng = np.random.default_rng(seed)
    R, coords = directed_hypercube((L, L))
    Th = rng.uniform(0.0, 2.0 * np.pi, size=R.shape) * R
    Pi = magnetic_precision(R, Th, m2=m2)
    Q = solenoidal_from_transport(R, Th, beta=beta)

    rows = []
    for half in range(2, max(3, L // 2)):
        lo, hi = L // 2 - half, L // 2 + half - 1
        A = [i for i, c in enumerate(coords) if lo <= c[0] <= hi and lo <= c[1] <= hi]
        I, b, E, _ = partition_triad(R, A)
        if len(I) == 0 or len(b) == 0 or len(E) == 0:
            continue
        r = boundary_effective_gap(Pi, Q, b, I, E)
        r.update({"half": half, "nA": len(A), "ndA": len(b), "nI": len(I)})
        rows.append(r)

    # m^2 dependence at fixed half
    m2_rows = []
    half_fixed = min(3, L // 2 - 1)
    lo, hi = L // 2 - half_fixed, L // 2 + half_fixed - 1
    A_fix = [i for i, c in enumerate(coords) if lo <= c[0] <= hi and lo <= c[1] <= hi]
    I_f, b_f, E_f, _ = partition_triad(R, A_fix)
    for m2_val in [0.2, 0.5, 1.0, 2.0, 5.0]:
        Pi_m = magnetic_precision(R, Th, m2=m2_val)
        Q_m = solenoidal_from_transport(R, Th, beta=beta)
        rm = boundary_effective_gap(Pi_m, Q_m, b_f, I_f, E_f)
        rm["m2"] = m2_val
        m2_rows.append(rm)

    # Assertions
    M_effs = [r["M_eff"] for r in rows]
    d_gammas = [r["d_gamma"] for r in rows]
    assert all(r["M_eff"] > 0 for r in rows), "M_eff must be positive"
    assert all(r["d_gamma"] < 0 for r in rows), "K_int must reduce boundary gap (d_gamma < 0)"
    # M_eff roughly non-decreasing with scale
    assert M_effs[-1] > M_effs[0], "M_eff should grow with core size"
    # |d_gamma| shrinks with m^2
    abs_dg = [abs(r["d_gamma"]) for r in m2_rows]
    assert abs_dg[-1] < abs_dg[0], "|d_gamma| should decrease with m^2"

    if verbose:
        print(f"[19] Schur boundary gap scaling (L={L}, m^2={m2}):")
        print(f"     half |A| |dA| |I|   M_eff    gamma_bdry  gamma_bdry0   d_gamma")
        for r in rows:
            print(f"     {r['half']:4d} {r['nA']:4d} {r['ndA']:4d} {r['nI']:4d}  "
                  f"{r['M_eff']:7.3f}  {r['gamma_bdry']:10.4f}  {r['gamma_bdry0']:10.4f}  "
                  f"{r['d_gamma']:+.4f}")
        print(f"     m^2 dependence (half={half_fixed}):")
        for r in m2_rows:
            print(f"       m^2={r['m2']:.1f}: M_eff={r['M_eff']:.3f}, "
                  f"d_gamma={r['d_gamma']:+.4f}")
        print(f"     OK: M_eff grows, d_gamma < 0, |d_gamma| falls with m^2")

    return {"scale_rows": rows, "m2_rows": m2_rows}


def schur_haar_u1_commutant_check(k=3, m=2, n_samples=2000, seed=7):
    """
    Numerical and algebraic verification of Propositions 7.1-7.3:
      1. Unique Killing-orthogonal central generator Q_orth = diag(1/k I_k, -1/m I_m) satisfies
         Tr(Q_orth W_orth) == 0 for all W_orth in su(m)_dA, whereas rank-1 terminal generator
         Q_v = diag(1/k I_k, -v v^dagger) = Q_orth + T_3 has spectrum (1/3, 1/3, 1/3, -1, 0)
         and [Q|_{I_A}, G_{k x k}] == 0.
      2. Monte Carlo Haar averaging over SU(k) annihilates G_{k x k} and X_{k x m}
         while preserving the full fixed subspace u(1)_inter (+) su(m)_dA (both Q_orth and W_orth).
      3. Proposition 7.3 screening check on the 4-node chain E={0} - b={1} - I={2, 3}:
         raw vectors u in ker(Pi_bI) have non-zero covariance with E_A (0.1882 at m^2=0.5,
         0.0123 at m^2=2.84), whereas every v in Pi_I(ker Pi_bI) has strictly zero covariance
         |v^dagger Sigma_IE| == 0.
    """
    rng = np.random.default_rng(seed)
    Q_orth = np.diag([1.0 / k] * k + [-1.0 / m] * m)
    Q_v = np.diag([1.0 / k] * k + [-1.0] + [0.0] * (m - 1))
    # Random traceless G in su(k)
    A_rand = rng.normal(size=(k, k)) + 1j * rng.normal(size=(k, k))
    G_k = 0.5 * (A_rand + A_rand.conj().T)
    G_k -= (np.trace(G_k) / k) * np.eye(k)
    comm_err = float(np.max(np.abs(Q_v[:k, :k] @ G_k - G_k @ Q_v[:k, :k])))

    # Random traceless boundary operator W_orth in su(m)
    B_rand = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m))
    W_m = 0.5 * (B_rand + B_rand.conj().T)
    W_m -= (np.trace(W_m) / m) * np.eye(m)
    W_blk = np.zeros((k + m, k + m), dtype=complex)
    W_blk[k:, k:] = W_m
    killing_orth_err = float(abs(np.trace(Q_orth @ W_blk)))

    # Haar invariant check on Q vs traceless block
    H_traceless = np.zeros((k + m, k + m), dtype=complex)
    H_traceless[:k, :k] = G_k
    acc_G = np.zeros_like(H_traceless)
    acc_Q = np.zeros_like(Q_v, dtype=complex)
    acc_W = np.zeros_like(W_blk, dtype=complex)
    for _ in range(n_samples):
        Z = (rng.normal(size=(k, k)) + 1j * rng.normal(size=(k, k))) / np.sqrt(2.0)
        U, R_qr = np.linalg.qr(Z)
        d = np.diag(R_qr)
        U *= d / np.abs(d)
        U /= np.linalg.det(U) ** (1.0 / k)
        blk_U = np.block([[U, np.zeros((k, m))], [np.zeros((m, k)), np.eye(m)]])
        acc_G += blk_U @ H_traceless @ blk_U.conj().T
        acc_Q += blk_U @ Q_v @ blk_U.conj().T
        acc_W += blk_U @ W_blk @ blk_U.conj().T
    haar_G_norm = float(np.linalg.norm(acc_G / n_samples, "fro"))
    haar_Q_err = float(np.max(np.abs(acc_Q / n_samples - Q_v)))
    haar_W_err = float(np.max(np.abs(acc_W / n_samples - W_blk)))

    # Proposition 7.3 check on 4-node chain E={0} - b={1} - I={2, 3}
    R_chain = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]], dtype=int)
    Pi_ch = magnetic_precision(R_chain, np.zeros_like(R_chain, dtype=float), m2=0.5)
    Sig_ch = np.linalg.inv(Pi_ch)
    Pi_I_ch = Pi_ch[2:, 2:]
    u_ker = np.array([0.0, 1.0], dtype=complex)  # in ker(Pi_bI) since Pi_{1,3} == 0
    v_screen = Pi_I_ch @ u_ker  # in Pi_I(ker Pi_bI)
    cov_raw_ker = float(np.abs(u_ker.conj() @ Sig_ch[2:, 0]))
    cov_screened = float(np.abs(v_screen.conj() @ Sig_ch[2:, 0]))

    return {
        "trace_Q_orth": float(np.trace(Q_orth)),
        "trace_Q": float(np.trace(Q_v)),
        "killing_orth_err": killing_orth_err,
        "commutator_err": comm_err,
        "haar_G_norm": haar_G_norm,
        "haar_Q_err": haar_Q_err,
        "haar_W_err": haar_W_err,
        "chain_cov_raw_ker": cov_raw_ker,
        "chain_cov_screened": cov_screened,
    }


def is_phase_admissible_l5(R, Theta, eps=0.5, d=2):
    """
    Check Phase epsilon-Admissibility Condition (L5) (Definition 8.1, Proposition 8.1):
      1. Principal-branch bound in tree gauge: 0 < eps < 2 * sin(pi / (2 * (d - 1))).
      2. For binary-diamond complexes (K_xy = 2), Wilson identity gives 1 - cos(Phi_12) = J_xy,
         so the chord is |U_D - 1| = sqrt(2 * J_xy) < eps iff max J_xy < eps^2 / 2.
    """
    branch_bound = 2.0 * np.sin(np.pi / (2.0 * max(1, d - 1)))
    if eps <= 0.0 or eps >= branch_bound:
        raise ValueError(f"eps={eps} violates principal-branch bound 0 < eps < {branch_bound:.6f} for d={d}.")
    _, _, J, _, _ = causal_phase_invariants(R, Theta)
    max_J = float(np.max(J)) if J.size else 0.0
    max_chord = float(np.sqrt(2.0 * max_J))
    return bool(max_chord < eps and max_J < 0.5 * (eps ** 2)), max_chord, max_J


def interpolate_2d_plaquette_landau(theta_bottom, theta_right, theta_top, theta_left, delta=0.1, n_pts=21):
    """
    2D Landau-Dirichlet continuum interpolation with smooth collar reparametrization Phi^* A
    on a single square cell [0, 1]^2 (Theorem 8.2, Witten Sec. 3).
    Verifies exact link holonomy reproduction and interior curl F_12 = Phi_P.
    """
    # Tree gauge on the 2-cell: gauge bottom, left, top edges to 0 so entire holonomy sits on right edge
    phi_p = ((theta_bottom + theta_right - theta_top - theta_left + np.pi) % (2 * np.pi)) - np.pi
    if abs(2.0 * np.sin(0.5 * phi_p)) >= 2.0:
        raise ValueError("Plaquette violates L5 admissibility branch cut.")

    # Smooth collar reparametrization s(t) with s(t) = 0 on [0, delta], 1 on [1-delta, 1]
    def s_collar(t):
        t = np.asarray(t, dtype=float)
        u = np.clip((t - delta) / (1.0 - 2.0 * delta), 0.0, 1.0)
        return 3.0 * u**2 - 2.0 * u**3

    def ds_collar(t):
        t = np.asarray(t, dtype=float)
        mask = (t > delta) & (t < 1.0 - delta)
        u = np.clip((t - delta) / (1.0 - 2.0 * delta), 0.0, 1.0)
        return np.where(mask, (6.0 * u * (1.0 - u)) / (1.0 - 2.0 * delta), 0.0)

    # 1. Exact Gauss-Legendre quadrature on the active interval [delta, 1 - delta]
    xi, wi = np.polynomial.legendre.leggauss(16)
    t_gl = 0.5 * (1.0 - 2.0 * delta) * xi + 0.5
    int_norm_gl = float(0.5 * (1.0 - 2.0 * delta) * np.sum(wi * ds_collar(t_gl)))
    hol_err_gl = abs(int_norm_gl * phi_p - phi_p)

    # 2. Composite trapezoidal rule on uniform grid (NumPy 1.x / 2.x compatible)
    grid = np.linspace(0.0, 1.0, n_pts)
    weights = ds_collar(grid)
    int_norm_trapz = float(_trapezoid(weights, grid))
    hol_err_trapz = abs(int_norm_trapz * phi_p - phi_p)
    return {
        "Phi_plaquette": float(phi_p),
        "collar_integral_norm": int_norm_gl,
        "holonomy_err": float(hol_err_gl),
        "trapezoid_integral_norm": int_norm_trapz,
        "trapezoid_holonomy_err": float(hol_err_trapz),
    }

# =====================================================================
# 9. SELF-TEST DRIVER: REPRODUCES SECTION 12 VERIFICATION TABLE
# =====================================================================

def _random_hasse(N, p=0.15, seed=0):
    """Random DAG with closure-based transitive reduction (a valid Hasse graph)."""
    rng = np.random.default_rng(seed)
    R0 = ((rng.random((N, N)) < p) & (np.arange(N)[:, None] < np.arange(N)[None, :])).astype(np.int64)
    reach2 = np.zeros((N, N), dtype=bool)
    pw = (R0 > 0).copy()
    for _ in range(2, N):
        pw = (pw @ (R0 > 0)) > 0
        if not pw.any():
            break
        reach2 |= pw
    return ((R0 > 0) & ~reach2).astype(np.int64)


def _brute_force_diamond_multiplicity(R):
    """Direct enumeration of elementary diamonds containing each Hasse edge."""
    N = len(R)
    d = np.zeros((N, N), dtype=np.int64)
    for x in range(N):
        for y in range(x + 1, N):
            if R[x, y] != 1:
                continue
            cnt = 0
            for w in range(N):
                if R[w, x] == 1:
                    for v in range(N):
                        if v != x and R[w, v] == 1 and R[v, y] == 1:
                            cnt += 1
            for z in range(N):
                if R[y, z] == 1:
                    for v in range(N):
                        if v != y and R[x, v] == 1 and R[v, z] == 1:
                            cnt += 1
            d[x, y] = cnt
    return d


def run_self_test(verbose=True):
    """
    Reproduces the Section 12.1 verification table of CPP v4.4 (Checks [1]-[19]).
    Returns True if all 18 checks pass within required numerical tolerances.
    """
    rng = np.random.default_rng(11)
    if verbose:
        print("=== cpp_v44_reference Self-Test Suite (CPP v4.4 Section 12.1, 19 checks) ===")

    # [1] d_diamond matrix formula vs brute-force enumeration + bipartite crown K_{2,2} check
    mism = 0
    for s in range(40):
        R = _random_hasse(24, p=0.15, seed=s)
        d_mat, _, _ = diamond_participation(R)
        mism += int(np.sum(np.abs(d_mat - _brute_force_diamond_multiplicity(R)) > 0))
    R_crown = np.array([[0, 0, 1, 1], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]], dtype=int)
    Th_crown = np.array([[0, 0, np.pi, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], dtype=float)
    d_cr, _, _ = diamond_participation(R_crown)
    phi_cr = float(
        np.linalg.slogdet(magnetic_precision(R_crown, Th_crown, m2=0.5))[1]
        - np.linalg.slogdet(magnetic_precision(R_crown, np.zeros_like(Th_crown), m2=0.5))[1]
    )
    if verbose:
        print(
            f"[1] d_diamond vs brute force on 40 Hasse graphs (N=24): mismatches = {mism}; "
            f"K_{{2,2}} crown: max(d_diamond)={int(d_cr.max())}, Phi_mag(pi)={phi_cr:.4f} (> 0)"
        )
    assert mism == 0 and int(d_cr.max()) == 0 and phi_cr > 0.05

    # [2] Wilson identity on a 6x6 lattice
    R6, coords6 = directed_hypercube((6, 6))
    Th6 = rng.uniform(0, 2 * np.pi, size=R6.shape) * R6
    w_err = verify_wilson_identity(R6, Th6)
    if verbose:
        print(f"[2] Wilson identity max error: {w_err:.2e}")
    assert w_err < 1e-10

    # [3] Gauge invariance of K, J, ||C||_F
    chi = rng.uniform(0, 2 * np.pi, size=len(R6))
    Th_g = (Th6 + np.outer(chi, np.ones_like(chi)) - np.outer(np.ones_like(chi), chi)) % (2 * np.pi)
    Th_g = Th_g * (R6 > 0)
    K1, _, J1, L1, _ = causal_phase_invariants(R6, Th6)
    K2, _, J2, L2, _ = causal_phase_invariants(R6, Th_g)
    dJ = float(np.max(np.abs(J1 - J2)))
    dL = abs(L1 - L2)
    if verbose:
        print(f"[3] Gauge invariance: max|dJ| = {dJ:.2e}, |d||C||^2| = {dL:.2e}")
    assert dJ < 1e-10 and dL < 1e-8

    # [4] Flat connection (Proposition 1.2) & causal-reversal symmetry (Lemma 2.4.1)
    Th_flat = (np.outer(-chi, np.ones_like(chi)) + np.outer(np.ones_like(chi), chi)) % (2 * np.pi)
    Th_flat = Th_flat * (R6 > 0)
    _, _, Jf, Lf, _ = causal_phase_invariants(R6, Th_flat)
    _, _, J0, L0, _ = causal_phase_invariants(R6, np.zeros_like(Th6))
    Pi_f = magnetic_precision(R6, Th_flat, m2=0.5)
    Pi_0 = magnetic_precision(R6, np.zeros_like(Th6), m2=0.5)
    dld = abs(float(np.linalg.slogdet(Pi_f)[1]) - float(np.linalg.slogdet(Pi_0)[1]))
    lem241 = verify_causal_parity_and_lemma_2_4_1(R6, Th6, m2=0.5)
    if verbose:
        print(
            f"[4] Flat connection & Lemma 2.4.1: sum J = {float(np.sum(Jf)):.2e}, "
            f"|d ln det Pi| = {dld:.2e}, sym_err = {lem241['sym_decomp_err']:.1e}, "
            f"causal-rev |d ln det Pi| = {lem241['logdet_rev_err']:.1e}, Q_W flip err = {lem241['q_flip_err']:.1e}"
        )
    assert float(np.sum(Jf)) < 1e-9 and abs(Lf - L0) < 1e-8 and dld < 1e-9
    assert lem241["sym_decomp_err"] < 1e-14 and lem241["logdet_rev_err"] < 1e-12 and lem241["q_flip_err"] < 1e-14

    # [5] Directed hypercubes (Proposition 3.5)
    for dims, expect in [((8, 8), 1), ((7, 7, 7), 3), ((5, 5, 5, 5), 6), ((4, 4, 4, 4, 4), 10)]:
        Kmax, dens, hasse = diamond_density_interior(dims)
        if verbose:
            print(f"[5] hypercube d={len(dims)}: Hasse={hasse}, K_max={Kmax}, interior K=2 counts={dens} (expect [{expect}])")
        assert hasse and Kmax == 2 and dens == [expect]

    # [6] Unified model (Definition 2.4) on a 7x7 lattice, m^2 = 0.5
    R7, coords7 = directed_hypercube((7, 7))
    Th7 = rng.uniform(0, 2 * np.pi, size=R7.shape) * R7
    Pi7 = magnetic_precision(R7, Th7, m2=0.5)
    herm = float(np.max(np.abs(Pi7 - Pi7.conj().T)))
    emin = float(np.min(np.linalg.eigvalsh(Pi7)))
    A_ball = [i for i, c in enumerate(coords7) if abs(c[0] - 3) + abs(c[1] - 3) <= 2]
    I7, b7, E7, _ = partition_triad(R7, A_ball)
    screen, cov_err = screening_and_mediated_covariance(Pi7, E7, b7, I7)
    if verbose:
        print(f"[6] Pi model (49 nodes): hermiticity = {herm:.1e}, lambda_min = {emin:.3f} (>= 0.5), screening = {screen:.1e}, cov formula err = {cov_err:.2e}")
    assert herm < 1e-12 and emin >= 0.5 - 1e-12 and screen == 0.0 and cov_err < 1e-12

    # [7] Kernel inclusion (Corollary 2.3)
    R9, coords9 = directed_hypercube((9, 9))
    Th9 = rng.uniform(0, 2 * np.pi, size=R9.shape) * R9
    Pi9 = magnetic_precision(R9, Th9, m2=0.5)
    A_ball3 = [i for i, c in enumerate(coords9) if c[0] >= 2]
    I9, b9, E9, _ = partition_triad(R9, A_ball3)
    viol_typ = kernel_inclusion_violation(Pi9, E9, b9, I9)
    A_block = [i for i, c in enumerate(coords9) if 1 <= c[0] <= 4 and 1 <= c[1] <= 4]
    I4, b4, E4, _ = partition_triad(R9, A_block)
    viol_bad = kernel_inclusion_violation(Pi9, E4, b4, I4)
    if verbose:
        print(f"[7] Kernel inclusion: |I|={len(I9)}, |dA|={len(b9)}; typical violation = {viol_typ:.2e} (expect 0); block-corner region = {viol_bad:.4f} (expect sqrt(2) = 1.4142)")
    assert viol_typ < 1e-8 and abs(viol_bad - np.sqrt(2.0)) < 1e-3

    # [8] Helmholtz decomposition and relaxation gap (Proposition 3.6)
    Qw = solenoidal_from_transport(R7, Th7, beta=1.0)
    anti = float(np.max(np.abs(Qw + Qw.conj().T)))
    Gam = np.eye(len(R7))
    B = (Gam + Qw) @ Pi7
    Sig = np.linalg.inv(Pi7)
    resid = float(np.max(np.abs(B @ Sig + Sig @ B.conj().T - 2 * Gam)))
    g0 = relaxation_gap(Pi7, Gam, np.zeros_like(Qw))
    gQ = relaxation_gap(Pi7, Gam, Qw)
    if verbose:
        print(f"[8] Helmholtz: anti-hermiticity = {anti:.1e}, covariance residual = {resid:.2e}, gamma(0) = {g0:.3f}, gamma(Q_W) = {gQ:.3f}")
    assert anti < 1e-12 and resid < 1e-10 and gQ >= g0 - 1e-12

    # [9] Exact entropy balance (Theorem 4.3) on a two-vertex subsystem
    sub = [int(i) for i in np.argwhere(R6 == 1)[[3]][0]]
    Rsub = R6[np.ix_(sub, sub)]
    Thsub = Th6[np.ix_(sub, sub)]
    Hm = transport_hermitian(Rsub, Thsub)
    lam = benettin_spectrum(Hm, 0.30, 0.25, 0.30, steps=20000, burn=500, seed=0)
    bal = entropy_balance_check(Hm, delta=0.30, g=0.25, noise=0.30, n_samples=100000, burn=150, seed=1, k=5)
    neg_sum = float(-np.sum(lam))
    if verbose:
        print(f"[9] Balance: lambda = {np.round(lam, 3).tolist()}, -sum(lambda) = {neg_sum:.3f}, -E ln|det DG| = {bal['minus_E_logdet']:.3f}, Delta_noise = {bal['Delta_noise']:.3f}, stationarity gap = {bal['stationarity_gap']:.4f}")
    assert abs(bal['Delta_noise'] - neg_sum) <= 0.05 and abs(bal['minus_E_logdet'] - neg_sum) <= 0.02

    # [10] Exact Gaussian linear control
    n = 4
    Ar = rng.normal(size=(n, n))
    Ar = Ar / (np.linalg.norm(Ar, 2) * 1.2)
    Sx = np.linalg.solve(np.eye(n * n) - np.kron(Ar, Ar), np.eye(n).reshape(-1)).reshape(n, n)
    Sx = 0.5 * (Sx + Sx.T)
    h_full = 0.5 * np.log(np.linalg.det(2 * np.pi * np.e * Sx))
    h_img = 0.5 * np.log(np.linalg.det(2 * np.pi * np.e * (Ar @ Sx @ Ar.T)))
    direct = h_full - h_img
    exact = float(-np.log(np.abs(np.linalg.det(Ar))))
    Lc = np.linalg.cholesky(Sx)
    Zs = rng.normal(size=(100000, n)) @ Lc.T
    xi = rng.normal(size=(100000, n))
    emp = knn_entropy(Zs @ Ar.T + xi, k=5) - knn_entropy(Zs @ Ar.T, k=5)
    if verbose:
        print(f"[10] Gaussian control: -ln|det A| = {exact:.4f}, direct entropy difference = {direct:.4f}, k-NN estimate = {emp:.4f}")
    assert abs(exact - direct) < 1e-8 and abs(emp - exact) < 0.05

    # [11] Rank-1 factorization and exact Woodbury edge-swap law (Proposition 6.2)
    Wc = R6 * np.exp(1j * Th6)
    Lth = np.diag((R6 + R6.T).sum(1)) - Wc - Wc.conj().T
    vv = np.zeros_like(Lth)
    for x, y in np.argwhere(R6 == 1):
        v = dipole_vector(len(R6), x, y, Th6[x, y])
        vv += np.outer(v, v.conj())
    fac_err = float(np.max(np.abs(Lth - vv)))
    Pi6 = magnetic_precision(R6, Th6, m2=0.5)
    edges = np.argwhere(R6 == 1)
    e_del = tuple(edges[len(edges) // 3])
    R2m = R6.copy()
    R2m[e_del] = 0
    K2m = R2m @ R2m
    cands = [(i, j) for i in range(len(R6)) for j in range(i + 1, len(R6)) if R2m[i, j] == 0 and K2m[i, j] == 0]
    e_add = cands[len(cands) // 2]
    Th_add = float(rng.uniform(0, 2 * np.pi))
    th_del = float(Th6[e_del])
    ratio_f = woodbury_edge_swap_ratio(Pi6, e_del, th_del, e_add, Th_add)[0]
    R6b = R6.copy()
    R6b[e_del] = 0
    R6b[e_add] = 1
    Th6b = Th6.copy()
    Th6b[e_del] = 0.0
    Th6b[e_add] = Th_add
    ratio_d = float(np.exp(np.linalg.slogdet(magnetic_precision(R6b, Th6b, m2=0.5))[1] - np.linalg.slogdet(Pi6)[1]))
    if verbose:
        print(f"[11] Rank-1 factorization err = {fac_err:.1e}; Woodbury {ratio_f:.12f} vs direct {ratio_d:.12f}")
    assert fac_err < 1e-12 and abs(ratio_f - ratio_d) < 1e-9 * max(1.0, abs(ratio_d))

    # [12] Loop expansion, triangle-freeness (Proposition 6.3) & Corollary 6.3.1 pi-plaquette benchmark
    worst = 0.0
    for s in range(40):
        Rs = _random_hasse(18, p=0.18, seed=100 + s)
        Ths = rng.uniform(0, 2 * np.pi, size=Rs.shape) * Rs
        d = loop_expansion_diagnostics(Rs, Ths, m2=0.5)
        worst = max(worst, abs(d['tr1']), abs(d['tr2_phase_diff']), abs(d['tr3_theta']), abs(d['tr3_zero']), -d['Phi_mag_exact'])
    tor = single_pi_plaquette_torus_benchmark(L=30, m2=0.5)
    if verbose:
        print(
            f"[12] Loop expansion: worst dev = {worst:.2e}; 30x30 torus pi-plaquette: "
            f"exact = {tor['exact_per_pi_plaquette']:.4f}, l=4 term = {tor['l4_leading_term']:.4f} "
            f"({100.0 * tor['l4_fraction']:.1f}% from l=4, {100.0 * tor['higher_loops_fraction']:.1f}% from l>=6)"
        )
    assert worst < 1e-10 and abs(tor["exact_per_pi_plaquette"] - 0.0372) < 5e-4

    # [13] Triadic Schur decomposition (Proposition 6.4)
    sch = triadic_schur_decomposition(Pi7, I7, b7, E7)
    if verbose:
        print(f"[13] Schur: decomposition error = {sch['decomposition_error']:.2e}, S_interface = {sch['S_interface_coupling']:.4f} (> 0)")
    assert sch['decomposition_error'] < 1e-10 and sch['S_interface_coupling'] > 0

    # [14] f_{K_eff=2} diagnostics on an 8x8 lattice
    R8, _ = directed_hypercube((8, 8))
    Th_zero = np.zeros_like(R8, dtype=float)
    Th_noise = (rng.normal(0, 0.1, size=R8.shape) % (2 * np.pi)) * R8
    Th_rand = rng.uniform(0, 2 * np.pi, size=R8.shape) * R8
    def f_K2(Th):
        K = R8 @ R8
        Ke = interval_local_path_quotient(R8, Th, eps_ker=0.30)
        act = K >= 2
        return float(np.sum(Ke[act] == 2) / max(1, int(act.sum())))
    f_al, f_no, f_ra = f_K2(Th_zero), f_K2(Th_noise), f_K2(Th_rand)
    if verbose:
        print(f"[14] f_K2 diagnostics (8x8): aligned = {f_al:.3f}, noise(0.1) = {f_no:.3f}, random = {f_ra:.3f}")
    assert f_al < 0.05 and f_ra > 0.8

    # [15] Admissibility (L0)-(L4)
    lat_ok = admissible(R6, nu=0.5, kmax=8)
    Rrand = _random_hasse(24, p=0.15, seed=7)
    rand_ok = admissible(Rrand, nu=0.5, kmax=4)
    Rkr = np.zeros((24, 24), dtype=np.int64)
    Rkr[:12, 12:] = (rng.random((12, 12)) < 0.5).astype(np.int64)
    kr_ok = admissible(Rkr, nu=0.5, kmax=8)
    if verbose:
        print(f"[15] Admissibility: lattice(nu=0.5,k=8) = {lat_ok}; sparse random(k=4) = {rand_ok}; two-layer KR sector = {kr_ok}")
    assert lat_ok and not kr_ok

    # [16] Cross-boundary Wilson identity W_cross = -Delta S_interface >= 0 (Proposition 6.5)
    cw = cross_wilson_action_identity(R7, Th7, I7, b7, E7, m2=0.5)
    if verbose:
        print(f"[16] Cross-Wilson identity (Prop. 6.5): W_cross = {cw['W_cross']:.4f} (>= 0), identity err = {cw['identity_err']:.2e}")
    assert cw["W_cross"] >= -1e-12 and cw["identity_err"] < 1e-12

    # [17] Schur-Haar fixed subspace, Killing orthogonality & screened subspace Pi_I(ker Pi_bI) (Props. 7.1-7.3)
    sh = schur_haar_u1_commutant_check(k=3, m=2, n_samples=2000, seed=7)
    sch7 = triadic_schur_decomposition(Pi7, I7, b7, E7)
    imp_comm = float(np.linalg.norm(sch7["K_int"] @ sch7["K_ext"] - sch7["K_ext"] @ sch7["K_int"], "fro"))
    if verbose:
        print(
            f"[17] Schur-Haar & Prop. 7.3: Tr(Q_orth W_orth) = {sh['killing_orth_err']:.1e}, "
            f"|[Q_I, G_3]| = {sh['commutator_err']:.1e}, Haar |Q_err| = {sh['haar_Q_err']:.1e}, "
            f"Haar |W_err| = {sh['haar_W_err']:.1e}, chain |Cov(ker Pi_bI, E)| = {sh['chain_cov_raw_ker']:.4f} vs "
            f"|Cov(Pi_I ker Pi_bI, E)| = {sh['chain_cov_screened']:.1e}, ||[K_int, K_ext]||_F = {imp_comm:.4f}"
        )
    assert (
        sh["killing_orth_err"] < 1e-14
        and sh["commutator_err"] < 1e-14
        and sh["haar_Q_err"] < 1e-12
        and sh["haar_W_err"] < 1e-12
        and sh["chain_cov_raw_ker"] > 0.1
        and sh["chain_cov_screened"] < 1e-14
        and imp_comm > 1e-4
    )

    # [18] Phase L5 admissibility (|U_D - 1| = sqrt(2 J_xy) < eps) & 2D Landau-Dirichlet collar interpolation
    ok_l5_003, chord_003, _ = is_phase_admissible_l5(R6, 0.03 * Th6, eps=0.5, d=2)
    ok_l5_005, chord_005, _ = is_phase_admissible_l5(R6, 0.05 * Th6, eps=0.5, d=2)
    ok_l5_rand, chord_rand, _ = is_phase_admissible_l5(R6, Th6, eps=0.5, d=2)
    interp = interpolate_2d_plaquette_landau(0.1, 0.2, -0.05, 0.15, delta=0.1, n_pts=401)
    if verbose:
        print(
            f"[18] L5 & Landau interpolation: 0.03*Th6 L5={ok_l5_003} (max|U-1|={chord_003:.3f}), "
            f"0.05*Th6 L5={ok_l5_005} (max|U-1|={chord_005:.3f} > 0.5), random L5={ok_l5_rand}, "
            f"Gauss-Legendre holonomy err={interp['holonomy_err']:.2e} (< 1e-12), "
            f"trapezoid(401) err={interp['trapezoid_holonomy_err']:.2e}"
        )
    assert ok_l5_003 and not ok_l5_005 and not ok_l5_rand and interp["holonomy_err"] < 1e-12

    # [19] Schur complement on triad acting on (Pi, Q_W): M_eff and boundary gap shift
    schur_boundary_gap_scaling_check(L=12, m2=0.5, beta=1.0, seed=7, verbose=verbose)

    if verbose:
        print("=== All 19 self-tests passed successfully ===\n")
    return True


# =====================================================================
# 10. SECTION 12.2 & 12.3 BENCHMARKS AND METROPOLIS V3/V4 DRIVER
# =====================================================================

def _random_su_n(n, rng, special=True):
    """Draw a Haar-random unitary matrix in U(n) or SU(n)."""
    Z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2.0)
    Q, R_qr = np.linalg.qr(Z)
    d = np.diag(R_qr)
    Q *= d / np.abs(d)
    if special:
        Q /= np.linalg.det(Q) ** (1.0 / n)
    return Q


def _s_interface_multicomponent(Pi, idx_I, idx_b, idx_E, d_rep=1):
    """Compute S_interface per component for a d_rep-dimensional gauge representation."""
    exp_idx = lambda lst: [d_rep * x + r for x in lst for r in range(d_rep)]
    Ii, bi, Ei = exp_idx(idx_I), exp_idx(idx_b), exp_idx(idx_E)
    blk = lambda u, v: Pi[np.ix_(u, v)]
    Pi_I, Pi_b, Pi_E = blk(Ii, Ii), blk(bi, bi), blk(Ei, Ei)
    S_dA = (
        Pi_b
        - blk(bi, Ii) @ np.linalg.inv(Pi_I) @ blk(Ii, bi)
        - blk(bi, Ei) @ np.linalg.inv(Pi_E) @ blk(Ei, bi)
    )
    return float(np.linalg.slogdet(Pi_b)[1] - np.linalg.slogdet(S_dA)[1]) / d_rep


def multigroup_w_cross_test(n_trials=120, m2=0.5, seed=42, verbose=True):
    """
    Reproduces Section 12.2(1): Universal non-negativity W_cross(U) = S_interface(I) - S_interface(U) >= 0
    across 120 random graphs and triads for each gauge group in {U(1), Z_2, U(2), SU(3)}.
    """
    rng = np.random.default_rng(seed)
    results = {}
    for grp, d_rep in [("U(1)", 1), ("Z_2", 1), ("U(2)", 2), ("SU(3)", 3)]:
        violations = 0
        strictly_positive = 0
        min_w = 0.0
        trials_done = 0
        attempt = 0
        while trials_done < n_trials:
            attempt += 1
            R = _random_hasse(18, p=0.22, seed=seed + 1000 * d_rep + attempt)
            A_nodes = rng.choice(18, size=8, replace=False)
            I_idx, b_idx, E_idx, _ = partition_triad(R, A_nodes)
            if len(I_idx) == 0 or len(b_idx) == 0 or len(E_idx) == 0:
                continue
            trials_done += 1
            N = len(R)
            deg = (R + R.T).sum(axis=1)
            Pi0 = np.kron(np.diag(m2 + deg) - (R + R.T), np.eye(d_rep, dtype=complex))
            W_blk = np.zeros((d_rep * N, d_rep * N), dtype=complex)
            for u, v in np.argwhere(R == 1):
                if grp == "U(1)":
                    U_uv = np.array([[np.exp(1j * rng.uniform(0.0, 2.0 * np.pi))]])
                elif grp == "Z_2":
                    U_uv = np.array([[float(rng.choice([-1.0, 1.0]))]])
                elif grp == "U(2)":
                    U_uv = _random_su_n(2, rng, special=False)
                else:
                    U_uv = _random_su_n(3, rng, special=True)
                W_blk[d_rep * u : d_rep * (u + 1), d_rep * v : d_rep * (v + 1)] = U_uv
            Pi_U = np.kron(np.diag(m2 + deg), np.eye(d_rep, dtype=complex)) - (W_blk + W_blk.conj().T)
            s0 = _s_interface_multicomponent(Pi0, I_idx, b_idx, E_idx, d_rep=d_rep)
            sU = _s_interface_multicomponent(Pi_U, I_idx, b_idx, E_idx, d_rep=d_rep)
            w_cross = s0 - sU
            min_w = min(min_w, w_cross)
            if w_cross < -1e-12:
                violations += 1
            if w_cross > 1e-9:
                strictly_positive += 1
        results[grp] = {
            "trials": n_trials,
            "violations": violations,
            "strictly_positive": strictly_positive,
            "min_W_cross": float(min_w),
        }
        if verbose:
            print(
                f"[Sec 12.2] Group {grp:5s}: violations = {violations}/{n_trials}, "
                f"strictly positive = {strictly_positive}/{n_trials}, min W_cross = {min_w:.2e}"
            )
        assert violations == 0
    return results


def _su2_rotation(axis, angle):
    axis = np.asarray(axis, dtype=float)
    axis = axis / np.linalg.norm(axis)
    sx = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sy = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    sz = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    gen = axis[0] * sx + axis[1] * sy + axis[2] * sz
    return np.cos(0.5 * angle) * np.eye(2, dtype=complex) + 1j * np.sin(0.5 * angle) * gen


def area_law_and_group_scaling_benchmark(verbose=True):
    """
    Reproduces Section 12.2(2):
      1. Area-law constants on the 22x22 directed square lattice at m^2 in {0.2, 0.5, 2.0}:
         reports both the single-square secant ratio on A = [6, 15]^2 (|dA| = 36) and the
         differential linear-regression slope across square cores of side 2h in {6, 8, 10, 12, 14}
         (|dA| in {20, 28, 36, 44, 52}), resolving the corner-intercept difference.
      2. Coherent U(1) vs non-abelian SU(2) surface-tension ratio sigma_U(1) / sigma_SU(2)
         on the 16x16 lattice at plaquette angle B = 0.20 for m^2 in {0.2, 0.5, 2.0}.
    """
    R22, coords22 = directed_hypercube((22, 22))
    idx22 = {c: i for i, c in enumerate(coords22)}
    deg22 = (R22 + R22.T).sum(axis=1)
    B_val = 0.05
    ThB = np.zeros(R22.shape, dtype=float)
    for x in range(22):
        for y in range(21):
            ThB[idx22[(x, y)], idx22[(x, y + 1)]] = B_val * x
    WB = R22 * np.exp(1j * ThB)

    area_law = {}
    for m2 in [0.2, 0.5, 2.0]:
        Pi0 = np.diag(m2 + deg22) - (R22 + R22.T)
        PiB = np.diag(m2 + deg22) - (WB + WB.conj().T)
        phi_mag_bulk = float(np.linalg.slogdet(PiB)[1] - np.linalg.slogdet(Pi0)[1])
        kappa_bulk = (phi_mag_bulk / (21 * 21)) / (B_val ** 2)

        b_sizes, s0_vals, ksig_vals = [], [], []
        for half in [3, 4, 5, 6, 7]:
            lo, hi = 11 - half, 10 + half
            A_sq = [i for i, c in enumerate(coords22) if lo <= c[0] <= hi and lo <= c[1] <= hi]
            I_sq, b_sq, E_sq, _ = partition_triad(R22, A_sq)
            s0 = _s_interface_multicomponent(Pi0, I_sq, b_sq, E_sq, d_rep=1)
            sB = _s_interface_multicomponent(PiB, I_sq, b_sq, E_sq, d_rep=1)
            b_sizes.append(len(b_sq))
            s0_vals.append(s0)
            ksig_vals.append((s0 - sB) / (B_val ** 2))

        # Index 2 corresponds to half=5 -> A = [6, 15]^2 with |dA| = 36
        a0_secant = s0_vals[2] / b_sizes[2]
        ksig_secant = ksig_vals[2] / b_sizes[2]
        a0_slope = float(np.polyfit(b_sizes, s0_vals, 1)[0])
        ksig_slope = float(np.polyfit(b_sizes, ksig_vals, 1)[0])
        area_law[m2] = {
            "a0_secant_36": a0_secant,
            "kappa_sigma_secant_36": ksig_secant,
            "a0_slope": a0_slope,
            "kappa_sigma_slope": ksig_slope,
            "kappa_bulk": kappa_bulk,
            "ratio_secant_to_bulk": ksig_secant / kappa_bulk,
            "ratio_slope_to_bulk": ksig_slope / kappa_bulk,
        }
        if verbose:
            print(
                f"[Sec 12.2 Area Law m^2={m2}] secant(|dA|=36): a0={a0_secant:.4f}, "
                f"kappa_sigma={ksig_secant:.4f} (ratio={ksig_secant/kappa_bulk:.2f}); "
                f"slope(|dA|=20..52): a0={a0_slope:.4f}, kappa_sigma={ksig_slope:.4f} "
                f"(ratio={ksig_slope/kappa_bulk:.2f})"
            )

    # U(1) vs SU(2) surface tension ratio on 16x16 lattice at plaquette angle phi = 0.20
    R16, coords16 = directed_hypercube((16, 16))
    idx16 = {c: i for i, c in enumerate(coords16)}
    deg16 = (R16 + R16.T).sum(axis=1)
    A16 = [i for i, c in enumerate(coords16) if 4 <= c[0] <= 11 and 4 <= c[1] <= 11]
    I16, b16, E16, _ = partition_triad(R16, A16)
    phi = 0.20
    N16 = len(R16)
    W_u1 = R16.astype(complex)
    for x in range(16):
        for y in range(15):
            W_u1[idx16[(x, y)], idx16[(x, y + 1)]] = np.exp(1j * phi * x)
    A_u1 = W_u1 + W_u1.conj().T

    rng_su2 = np.random.default_rng(14)
    W_su2 = np.zeros((2 * N16, 2 * N16), dtype=complex)
    for u, v in np.argwhere(R16 == 1):
        W_su2[2 * u : 2 * u + 2, 2 * v : 2 * v + 2] = np.eye(2, dtype=complex)
    for y in range(15):
        U_prod = np.eye(2, dtype=complex)
        for x in range(16):
            u, v = idx16[(x, y)], idx16[(x, y + 1)]
            W_su2[2 * u : 2 * u + 2, 2 * v : 2 * v + 2] = U_prod
            U_step = _su2_rotation(rng_su2.normal(size=3), 2.0 * phi)
            U_prod = U_step @ U_prod
    A_su2 = W_su2 + W_su2.conj().T

    u1_su2_ratios = {}
    for m2 in [0.2, 0.5, 2.0]:
        Pi0 = np.diag(m2 + deg16) - (R16 + R16.T)
        Pi_u1 = np.diag(m2 + deg16) - A_u1
        Pi_su2 = np.kron(np.diag(m2 + deg16), np.eye(2, dtype=complex)) - A_su2
        s0 = _s_interface_multicomponent(Pi0, I16, b16, E16, d_rep=1)
        su1 = _s_interface_multicomponent(Pi_u1, I16, b16, E16, d_rep=1)
        ssu2 = _s_interface_multicomponent(Pi_su2, I16, b16, E16, d_rep=2)
        u1_su2_ratios[m2] = float((s0 - su1) / (s0 - ssu2))
        if verbose:
            print(f"[Sec 12.2 U(1)/SU(2) m^2={m2}] sigma_U(1) / sigma_SU(2) = {u1_su2_ratios[m2]:.2f}")

    return {"area_law": area_law, "u1_su2_ratios": u1_su2_ratios}


def _external_f_null(R, E_idx):
    """Compute fraction of diamond-free Hasse edges f_null(E_A) inside external zone E_A."""
    d_diam, _, _ = diamond_participation(R)
    E_mask = np.zeros(len(R), dtype=bool)
    E_mask[E_idx] = True
    ext_edges = (R == 1) & np.outer(E_mask, E_mask)
    n_ext = int(np.sum(ext_edges))
    if n_ext == 0:
        return 0.0
    return float(np.sum(ext_edges & (d_diam == 0)) / n_ext)


def run_metropolis_v3_v4_driver(
    L=8,
    nu=0.5,
    kmax=8,
    T=0.5,
    m2=0.5,
    eta_field=1.0,
    phi_core=np.pi,
    n_steps=400,
    burn_in=150,
    audit_every=200,
    n_seeds=4,
    seed_base=100,
    verbose=True,
):
    """
    Metropolis-Hastings driver for Protocols V3 and V4 (Section 12.3):
      - Co-evolves (R, Theta) in A(nu, k_max) under F_joint = F_struct + eta_field * ln det Pi
        at temperature T (with n_bos = eta_field / T) using exact 2x2 Woodbury edge swaps.
      - Audits accumulated Woodbury ln det Pi against direct slogdet every `audit_every` steps.
      - Measures Delta f_null(E_A) against uncoupled control (eta_field = 0) and cross-boundary
        Wilson action W_cross(phi_core) = -Delta S_interface(phi_core) >= 0.
    """
    R_init, coords = directed_hypercube((L, L))
    idx_map = {c: i for i, c in enumerate(coords)}
    lo, hi = L // 2 - 2, L // 2 + 1
    A_core = [i for i, c in enumerate(coords) if lo <= c[0] <= hi and lo <= c[1] <= hi]
    I_idx, b_idx, E_idx, _ = partition_triad(R_init, A_core)
    core_set = set(A_core)

    def _run_chain(eta_val, seed):
        rng = np.random.default_rng(seed)
        R = R_init.copy()
        Theta = rng.uniform(0.0, 2.0 * np.pi, size=R.shape) * R
        # Impose frustrated flux phi_core on central core plaquette
        c0 = (L // 2 - 1, L // 2 - 1)
        c1 = (L // 2, L // 2 - 1)
        c2 = (L // 2, L // 2)
        c3 = (L // 2 - 1, L // 2)
        Theta[idx_map[c0], idx_map[c1]] = phi_core
        Theta[idx_map[c1], idx_map[c2]] = 0.0
        Theta[idx_map[c0], idx_map[c3]] = 0.0
        Theta[idx_map[c3], idx_map[c2]] = 0.0

        F_struct, F_joint, logdet_curr = structural_and_joint_cost(
            R, Theta, eta_field=eta_val, m2=m2, T=T
        )
        max_woodbury_drift = 0.0
        f_null_samples = []
        w_cross_samples = []

        for step in range(1, n_steps + 1):
            # Attempt either an external phase update or an external Woodbury edge swap
            if rng.random() < 0.5:
                ext_edges = [
                    (u, v) for u, v in np.argwhere(R == 1) if not (u in core_set and v in core_set)
                ]
                if ext_edges:
                    e_mod = ext_edges[rng.integers(len(ext_edges))]
                    Th_prop = Theta.copy()
                    Th_prop[e_mod] = (Th_prop[e_mod] + rng.normal(0.0, 0.35)) % (2.0 * np.pi)
                    _, F_prop, ld_prop = structural_and_joint_cost(
                        R, Th_prop, eta_field=eta_val, m2=m2, T=T
                    )
                    if np.log(rng.random()) < -(F_prop - F_joint) / T:
                        Theta = Th_prop
                        F_joint = F_prop
                        logdet_curr = ld_prop
            else:
                ext_edges = [(u, v) for u, v in np.argwhere(R == 1) if u in E_idx and v in E_idx]
                if ext_edges:
                    e_del = ext_edges[rng.integers(len(ext_edges))]
                    u_cand, v_cand = sorted(rng.choice(E_idx, size=2, replace=False))
                    if R[u_cand, v_cand] == 0 and abs(u_cand - v_cand) <= L + 2:
                        R_prop = R.copy()
                        R_prop[e_del] = 0
                        R_prop[u_cand, v_cand] = 1
                        if admissible(R_prop, nu=nu, kmax=kmax):
                            th_add = float(rng.uniform(0.0, 2.0 * np.pi))
                            Th_prop = Theta.copy()
                            Th_prop[e_del] = 0.0
                            Th_prop[u_cand, v_cand] = th_add
                            if eta_val > 0.0:
                                Pi_curr = magnetic_precision(R, Theta, m2=m2)
                                ratio_w, _, _, _ = woodbury_edge_swap_ratio(
                                    Pi_curr, e_del, float(Theta[e_del]), (u_cand, v_cand), th_add
                                )
                                ld_prop = logdet_curr + float(np.log(max(1e-30, ratio_w)))
                                F_s_prop, _, _ = structural_and_joint_cost(
                                    R_prop, Th_prop, eta_field=0.0, m2=m2, T=T
                                )
                                F_prop = F_s_prop + eta_val * ld_prop
                            else:
                                F_s_prop, F_prop, ld_prop = structural_and_joint_cost(
                                    R_prop, Th_prop, eta_field=0.0, m2=m2, T=T
                                )
                            if np.log(rng.random()) < -(F_prop - F_joint) / T:
                                R = R_prop
                                Theta = Th_prop
                                F_joint = F_prop
                                logdet_curr = ld_prop

            if eta_val > 0.0 and step % audit_every == 0:
                ld_exact = float(np.linalg.slogdet(magnetic_precision(R, Theta, m2=m2))[1])
                max_woodbury_drift = max(max_woodbury_drift, abs(logdet_curr - ld_exact))
                logdet_curr = ld_exact

            if step > burn_in and step % 10 == 0:
                f_null_samples.append(_external_f_null(R, E_idx))
                cw = cross_wilson_action_identity(R, Theta, I_idx, b_idx, E_idx, m2=m2)
                w_cross_samples.append(cw["W_cross"])

        return (
            float(np.mean(f_null_samples)),
            float(np.mean(w_cross_samples)),
            float(max_woodbury_drift),
        )

    df_list, wc_list, max_drift = [], [], 0.0
    for s in range(n_seeds):
        f_eta, wc_eta, drift = _run_chain(eta_field, seed_base + s)
        f_0, _, _ = _run_chain(0.0, seed_base + 1000 + s)
        df_list.append(f_eta - f_0)
        wc_list.append(wc_eta)
        max_drift = max(max_drift, drift)

    df_mean = float(np.mean(df_list))
    df_se = float(np.std(df_list, ddof=1) / np.sqrt(n_seeds)) if n_seeds > 1 else 0.0
    wc_mean = float(np.mean(wc_list))
    wc_se = float(np.std(wc_list, ddof=1) / np.sqrt(n_seeds)) if n_seeds > 1 else 0.0
    z_df = df_mean / max(1e-12, df_se)
    verdict_v3 = "FOLLOW" if abs(z_df) > 3.0 else "UNDECIDED"
    if verbose:
        print(
            f"[Sec 12.3 V3/V4 Driver] eta_field={eta_field} (n_bos={eta_field/T:.1f}), "
            f"max Woodbury drift={max_drift:.2e}: Delta f_null = {df_mean:+.4f} +/- {df_se:.4f} "
            f"(z={z_df:+.2f} sigma -> {verdict_v3}), W_cross = {wc_mean:+.4f} +/- {wc_se:.4f} (> 0)"
        )
    assert max_drift < 1e-10 and wc_mean > 0.0
    return {
        "eta_field": eta_field,
        "n_bos": eta_field / T,
        "Delta_f_null_mean": df_mean,
        "Delta_f_null_se": df_se,
        "z_score_v3": z_df,
        "verdict_v3": verdict_v3,
        "W_cross_mean": wc_mean,
        "W_cross_se": wc_se,
        "max_woodbury_drift": max_drift,
    }


class _Tee:
    """Write simultaneously to console and to a log file."""
    def __init__(self, *streams):
        self.streams = streams
    def write(self, data):
        for s in self.streams:
            s.write(data)
            s.flush()
    def flush(self):
        for s in self.streams:
            s.flush()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CPP v4.4 Reference Implementation & Verification Suite")
    parser.add_argument(
        "--mode",
        choices=["selftest", "multigroup", "arealaw", "v3v4", "all"],
        default="selftest",
        help="Verification suite to execute (default: selftest)",
    )
    parser.add_argument(
        "--log",
        default=None,
        help="Path to results log file (default: cpp_v44_results_YYYYMMDD_HHMMSS.txt)",
    )
    args = parser.parse_args()

    if args.log is None:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        args.log = f"cpp_v44_results_{stamp}.txt"

    log_path = os.path.abspath(args.log)
    log_file = open(log_path, "w", encoding="utf-8")
    old_stdout = sys.stdout
    sys.stdout = _Tee(old_stdout, log_file)

    try:
        print(f"CPP v4.4 results log: {log_path}")
        print(f"Mode: {args.mode}")
        print(f"Started: {datetime.now().isoformat(timespec='seconds')}")
        print("=" * 72)
        if args.mode in ("selftest", "all"):
            run_self_test(verbose=True)
        if args.mode in ("multigroup", "all"):
            multigroup_w_cross_test(n_trials=120, seed=42, verbose=True)
        if args.mode in ("arealaw", "all"):
            area_law_and_group_scaling_benchmark(verbose=True)
        if args.mode in ("v3v4", "all"):
            run_metropolis_v3_v4_driver(n_steps=250, burn_in=100, n_seeds=4, verbose=True)
        print("=" * 72)
        print(f"Finished: {datetime.now().isoformat(timespec='seconds')}")
        print(f"Results saved to: {log_path}")
    finally:
        sys.stdout = old_stdout
        log_file.close()
        print(f"\nResults also saved to: {log_path}")
