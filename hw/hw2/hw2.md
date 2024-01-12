# HW2

## 1

$Suppose\ m_1=(x_1, y_1), m_2=(x_2, y_2)\in C_1\times C_2\\
\because C_1, C_2\ are\ convex\\
\therefore \forall t\in [0, 1], tx_1+(1-t)x_2\in C_1, ty_1+(1-t)y_2\in C_2\\
\therefore \forall t\in [0, 1], tm_1+(1-t)m_2\in C_1\times C_2\\
\therefore C_1\times C_2\ is\ convex$
$

## 2

$Suppose\ x_1, x_2\in f^{-1}(D),i.e.\ Ax_1+b\in D, Ax_2+b\in D\\
\because D\ is\ convex\\
\therefore\forall \theta\in [0, 1], A(\theta x_1+(1-\theta)x_2)+b=\theta(Ax_1+b)+(1-\theta)(Ax_2+b)\in D\\
\therefore \theta x_1+(1-\theta)x_2\in f^{-1}(D)\\
\therefore f^{-1}(D)\ is\ convex
$

## 3

$Prove\ by\ inuction$
$\textbf{Induction\ Basis}:When\ n=2, statement\ is\ obviously\ true\ by\ definition$
$\textbf{Induction\ Step}:Assume\ when\ n=k\geq 2, statement\ is\ true$
$When\ n = k+1$
$$
\begin{align}
\sum_{i=1}^{k+1}\theta_ix_i&=\theta_1x_1+\theta_2x_2+\sum_{i=3}^{k+1}\theta_ix_i\\
&=(\theta_1+\theta_2)(\frac{\theta_1}{\theta_1+\theta_2}x_1+\frac{\theta_2}{\theta_1+\theta_2}x_2)+\sum_{i=3}^{k+1}\theta_ix_i\\
&(x_2=\frac{\theta_1}{\theta_1+\theta_2}x_1+\frac{\theta_2}{\theta_1+\theta_2}x_2\in C)\\
&(\theta_2=\theta_1+\theta_2)\\
&=\sum_{i=2}^{k+1}\theta_ix_i\in C
\end{align}
$$
$Therefore, statement\ is\ true\ when\ n=k+1$
$Q.E.D.$

## 4

(a)
$Suppose\ x=\sum_{i=1}^m\theta_ix_i\in C, y=\sum_{i=1}^nt_iy_i\in C$
$\forall \alpha\in [0,1],$
$$
\alpha x+(1-\alpha)y=\sum_{i=1}^m\alpha\theta_ix_i+\sum_{i=1}^n(1-\alpha)t_iy_i\\
$$
$
\sum_{i=1}^m\alpha\theta_i+\sum_{i=1}^n,(1-\alpha)t_i=1\\
\alpha\theta_i,\ (1-\alpha)t_i\geq 0,\quad
x_i, y_i\in C\\
$
$
\therefore \alpha x+(1-\alpha)y\in C\\
\therefore C\ is\ convex
$

(b)
$\because C\ is \ convex, S\subset C$
$\therefore conv\ S\subset C$
$
\because C\ is\ convex,\ from\ the\ statement\ in\ Problem\ 3， we\ can\ claim\ that\ C\subset conv\ S\\
$
$Therefore, C=conv\ S$

## 5

$$
\begin{align}
V=&\{x\in R^n\mid \Vert x-x_0\Vert_2\leq \Vert x-x_i\Vert_2, i=1,2,...,K\}\\
=&\{x\in R^n\mid \Vert x-x_0\Vert_2^2\leq \Vert x-x_i\Vert_2^2, i=1,2,...,K\}\\
=&\{x\in R^n\mid (x_i-x_0)^Tx\leq \frac{1}{2}(x_i^Tx_i-x_0^Tx_0), i=1,2,...,K\}\\
&(Suppose\ A_i=(x_i-x_0)^T, b_i=\frac{1}{2}(x_i^Tx_i-x_0^Tx_0))\\
=&\{x\in R^n\mid A_ix\leq b_i, i=1,2,...,K\}\\
\end{align}
$$
$Therefore, V\ is\ a\ polyhedron$
