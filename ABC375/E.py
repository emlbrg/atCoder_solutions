from pulp import (
    LpBinary,
    LpMinimize,
    LpProblem,
    LpVariable,
    PULP_CBC_CMD,
    lpDot,
    value,
)

num_vars = int(input())

model = LpProblem(name="ABC375_E", sense=LpMinimize)
var_X = [LpVariable(name="var_X" + str(i), cat=LpBinary) for i in range(num_vars)]
var_Y = [LpVariable(name="var_Y" + str(i), cat=LpBinary) for i in range(num_vars)]
var_Z = [LpVariable(name="var_Z" + str(i), cat=LpBinary) for i in range(num_vars)]
objective_value = 0
weights = []

for index in range(num_vars):
    model += var_X[index] + var_Y[index] + var_Z[index] == 1
    action_type, weight = map(int, input().split())
    weights.append(weight)

    if action_type == 1:
        objective_value += var_Y[index] + var_Z[index]
    elif action_type == 2:
        objective_value += var_X[index] + var_Z[index]
    else:
        objective_value += var_X[index] + var_Y[index]

model += lpDot(weights, var_X) == lpDot(weights, var_Y)
model += lpDot(weights, var_Z) == lpDot(weights, var_Y)
model += objective_value

status = model.solve(PULP_CBC_CMD(msg=False, timeLimit=2.5))

if status == 1:
    print(int(value(model.objective)))
else:
    print(-1)
