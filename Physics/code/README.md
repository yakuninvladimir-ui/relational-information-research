# CPP v4.4 — Reference Implementation

Эталонная реализация **Causal Phase Program v4.4**.

## Файлы

| Файл | Описание |
|------|----------|
| `cpp_v44_reference.py` | Полный reference-код: алгебра §§1–8, self-test [1]–[19], benchmarks §12.2–12.3 |
| `results/cpp_v44_results_all.txt` | Канонический лог прогона `--mode all` (19 checks + multigroup + area-law + V3/V4) |

## Зависимости

```
numpy
scipy
```

## Запуск

```bash
# Только self-test (checks 1–19)
python cpp_v44_reference.py --mode selftest

# Полный набор (§12.1 + §12.2 + §12.3)
python cpp_v44_reference.py --mode all

# Отдельные блоки
python cpp_v44_reference.py --mode multigroup
python cpp_v44_reference.py --mode arealaw
python cpp_v44_reference.py --mode v3v4

# Свой путь к логу
python cpp_v44_reference.py --mode all --log my_results.txt
```

Результаты пишутся и в консоль, и в файл (по умолчанию `cpp_v44_results_YYYYMMDD_HHMMSS.txt`).

## Покрытие

- **§12.1** — 19 численных проверок (FOLLOW)
- **§12.2** — multigroup \(W_{\mathrm{cross}}\ge 0\), area-law, \(\sigma_{U(1)}/\sigma_{SU(2)}\) (FOLLOW)
- **§12.3** — Metropolis V3/V4 driver (Woodbury drift = 0, \(W_{\mathrm{cross}}>0\); \(\Delta f_{\mathrm{null}}\) = UNDECIDED)

Нормативный родитель: [`../Causal_Phase_Program_v4.4.md`](../Causal_Phase_Program_v4.4.md).
