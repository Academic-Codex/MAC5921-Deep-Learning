import os, socket, sys, time
print("=== SLURM SMOKE ===")
print("host:", socket.gethostname())
print("cwd:", os.getcwd())
print("args:", sys.argv[1:])
print("SLURM_JOB_ID:", os.getenv("SLURM_JOB_ID"))
for i in range(3):
    print("tick", i+1); time.sleep(1)
print("=== OK ===")


# Exercicio_Teste/test_figs.py
import os, matplotlib.pyplot as plt
os.makedirs("figures", exist_ok=True)
plt.plot([1,2,3],[1,4,9])
plt.title("ok")
plt.savefig("figures/test.png")
print("salvou em figures/test.png")