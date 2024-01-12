# HW4

## 1

$
(a)\ neither.\ Domain\ is\ convex\ and\ open.$
$$
f(x)=x^T\begin{bmatrix}
2&0&\frac{1}{2}\\
0&1&1\\
\frac{1}{2}&1&\frac{1}{2}
\end{bmatrix}x
$$

```python
import numpy as np

x = np.array([[2, 0 ,1/2], [0,1,1],[1/2,1,1/2]])
print(np.linalg.eigvals(x))
>>> [-0.34819639  2.25909935  1.58909704]
```

$
(b)\ convex.\ Domain\ is\ open\ and\ convex.
$

$$\nabla^2f(x)=
\begin{bmatrix}
\frac{2}{x_1^3x_2} & \frac{1}{x_1^2x_2^2}\\
\frac{1}{x_1^2x_2^2} & \frac{2}{x_1x_2^3}
\end{bmatrix}
\succ 0
$$

$(c)\ neither.\ Domain\ is\ open\ and\ convex.$

$$\nabla^2f(x)=
\begin{bmatrix}
0&1\\
1&0
\end{bmatrix}
$$

$(d)\ convex.\ Domain\ is\ open\ and\ convex.$

$$\nabla^2f(x)=
\begin{bmatrix}
0&-\frac{1}{x_2^2}\\
-\frac{1}{x_2^2}&\frac{2x_1}{x_2^3}
\end{bmatrix}
\succeq 0
$$

$(e)neither.\ \ Domain\ is\ open\ and\ convex.$
$\alpha = 0\ or \ 1, f(x)\ is\ obviously\ convex\ and\ concave.$
$otherwise:$
$$\nabla^2f(x)=
\alpha(1-\alpha)
\begin{bmatrix}
-x_1^{-\alpha-2}x_2^{1-\alpha} & x_1^{\alpha-1}x_2^{-\alpha}\\
x_1^{\alpha-1}x_2^{-\alpha} &  
-x_1^{\alpha}x_2^{-1-\alpha}
\end{bmatrix}
$$

## 2

$(a)\ \forall x\neq y\in \mathbb{R}
$
$$
\begin{align}
&\quad f(y)>f(x)+\nabla f(x)^T(y-x)\\
\Leftrightarrow&\quad y^4>x^4+4x^3(y-x)\\
\Leftrightarrow&\quad y^4-4x^3y+3x^4>0\\
\Leftrightarrow&\quad (y-x)^2(y^2+2xy+3x^2)>0\\
\Leftrightarrow&\quad (y-x)^2((y+x)^2+2x^2)>0\\
\end{align}
$$

$By\ the\ first-order\ condition,\ f(x)\ is\ convex.$

$(b)\ \forall x\neq y\in \mathbb{R^2}$
$$
\begin{align}
&\quad f(y)>f(x)+\nabla f(x)^T(y-x)\\
\Leftrightarrow&
\quad y_1^2+y_2^4>x_1^2+x_2^4+2x_1(y_1-x_1)+4x_2^3(y_2-x_2)\\
\Leftrightarrow&
\quad y_1^2-2x_1y_1+x_1^2+y_2^4-4x_2^3y_2+3x_2^4>0\\
\Leftrightarrow&
\quad (y_1-x_1)^2+(y_2-x_2)^2(y_2^2+2x_2y_2+3x_2^2)>0\\
\Leftrightarrow&
\quad (y_1-x_1)^2+(y_2-x_2)^2((y_2+x_2)^2+2x_2^2)>0\\
\end{align}
$$
$By\ the\ first-order\ condition,\ f(x)\ is\ convex.$

## 3

$\forall x,y\in\text{dom}f,\ \forall \theta\in[0,1]$

$$
\begin{align}
f(\theta x+\bar{\theta}y)& \leq
\theta f(x)+\bar{\theta}f(y)\\
&\leq max\{f(x),f(y)\}\\
&<\infty
\end{align}
$$
$\therefore\ \theta x+\bar{\theta}y\in \text{dom}f$
$\therefore \text{dom}f\ is\ convex.$

## 4

$Assume\ f(x)=x_1logx_1+x_2logx_2, \text{dom}f=\mathbb{R}_{++}^2$
$
\forall x,y\in\text{dom}f,\ \forall \theta\in[0,1]
$
$$
\nabla^2 f(x)=\begin{bmatrix}
\frac{1}{x_1} & 0\\
0 & \frac{1}{x_2}
\end{bmatrix}
\succ 0
$$
$\therefore f(x)\ is\ convex.$
$\because S\ is\ a\ sublevel\ set\ of\ f$
$\therefore S\ is\ convex.$

## 5

$(a)\ No.\ g\ is\ not\ convex.$
$$
\nabla^2 g(x)=\begin{bmatrix}
2+e^{x_1+x_2}&3+e^{x_1+x_2}\\
3+e^{x_1+x_2}&2+e^{x_1+x_2}
\end{bmatrix}
$$
$(b)\ No.\ h\ is\ not\ affine\ function.$
