# Automate AWS Resource

Funções lambdas para ligar e desligar recursos como ec2 e rds em dias úteis, os recursos marcados com a tag `turnOff=true` irá ser afetado.
Os recursos serão ligados de segunda a sexta às 08h (UTC-3) e desligados às 21h (UTC-03)
