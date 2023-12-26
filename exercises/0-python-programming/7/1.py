import solow
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 6)

s1 = solow.Solow()
s2 = solow.Solow(k=8.0)

T = 60
fig, ax = plt.subplots(figsize=(9, 6))

ax.plot([s1.steady_state()]*T, 'k-', label='steady state')

for s in s1, s2:
    lb = f"capital series from initial state {s.k}"
    ax.plot(s.generate_sequence(T), 'o-', lw=2, alpha=0.6, label=lb)

ax.set_xlabel('$t$', fontsize=14)
ax.set_ylabel('$k_t$', fontsize=14)
ax.legend()
plt.show()
