Comandos para criar um kernel-spec:

Comando para verificar a criação de um kernel-spec:
jupyter kernelspec list
# ou
python3 -m remote_ikernel manage --show

Comando para deletar um kernel-spec:

python3 -m remote_ikernel manage --delete "Sisko CPU4 (2h)"

Comandos para alterar os parametros de um kernel-spec:
--remote-precmd 'module load cuda/12.2'
--remote-launch-args '-p all --cpus-per-task=4 --gres=gpu:1 -t 02:00:00'

Comando para criar um remote-venv:

Comando para executar um job python em um nó HPC:
