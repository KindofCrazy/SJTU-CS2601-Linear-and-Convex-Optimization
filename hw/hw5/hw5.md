# HW5

## 1

$$
\begin{aligned}
\min_{x_1,x_2,s} \quad & 2x_1-3x_2\\
\textrm{s.t.}\quad & x_1+x_2=7\\
& x_1-2x_2+s=4\\
& x_1\geq 0,\ s\geq 0
\end{aligned}
$$

## 2

$(a)$

```python
status: optimal
optimal value 0.6000000000007311
optimal var 0.40000000000049696 0.20000000000023407
```

$(b)$

```python
status: unbounded
optimal value -inf
optimal var None None
```

$(c)$

```python
status: optimal
optimal value 0.0
optimal var 0.0 1.0
```

$(d)$

```python
status: optimal
optimal value 0.3333333333333333
optimal var 0.3333333333333333 0.3333333333333333
```

$(e)$

```python
status: optimal
optimal value 0.5000000000000002
optimal var 0.5000000000000001 0.1666666666666667
```

## 3

$$
\begin{aligned}
\min_{\boldsymbol{x,t}} \quad & \boldsymbol{1^Tt}\\
\textrm{s.t.}\quad & \boldsymbol{t}\succeq \boldsymbol{Ax}-\boldsymbol{b}\\
& \boldsymbol{t}\succeq -(\boldsymbol{Ax}-\boldsymbol{b})\\
& \boldsymbol{-1}\preceq \boldsymbol{x}\preceq \boldsymbol{1}\\
\end{aligned}
$$

$(b)$

```python
status: optimal
optimal value 17.99999999894348
optimal var [ 1. -1.]
```

$(c)$

```python
status: optimal
optimal value 17.999999999998796
optimal var: x:[ 1. -1.], t:[9. 6. 3.]
```

## 4

$(a)$

$\boldsymbol{w}=\begin{bmatrix}
    \frac{3}{2}\\
    2
\end{bmatrix}$

$(b)$

$t=1:$
$The\ solution \ is\ not\ same\ as\ (a),\ and\ the\ solution\ is\ sparse.$

```python
status: optimal
optimal value 9.00000014741406
optimal var: w:[9.99907131e-01 9.28426676e-05]
```

$t=10:$
$The\ solution \ is\ same\ as\ (a),\ and\ the\ solution\ is\ not\ sparse.$

```python
status: optimal
optimal value 4.000000000167633
optimal var: w:[1.50000631 2.00000291]
```

$(c)$

$t=1:$
$The\ solution \ is\ not\ same\ as\ (a),\ and\ the\ solution\ is\ sparse.$

```python
status: optimal
optimal value 9.000000111722128
optimal var: w:[9.99922348e-01 7.76315394e-05]
```

$t=10:$

$The\ solution \ is\ not\ same\ as\ (a),\ and\ the\ solution\ is\ not\ sparse.$

```python
status: optimal
optimal value 4.0912451063716935
optimal var: w:[1.43246941 1.72980824]
```
