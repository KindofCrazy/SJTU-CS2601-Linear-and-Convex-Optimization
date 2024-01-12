# HW9

## 1

$(a)$
$step=-[\nabla^2f(x)]^{-1}\nabla f(x)=-\frac{1}{3}(x-a)$

$(b)$
$$
\begin{aligned}
y_{k+1}&=\ \mid x_{k+1}-a\mid\\
&=\ \mid x_k - \frac{1}{3}(x_k-a)-a\mid\\
&=\ \mid \frac{2}{3}(x_k-a)\mid\\
&=\ \frac{2}{3}y_k
\end{aligned}
$$

$(c)$
$\mid x_k-a\mid=(\frac{2}{3})^k\mid x_0-a\mid$
$Thus\ \mid x_k-a\mid\ decays\ to\ zero\ expotentially$

## 2

$(a)$
$f(x)\ is\ obviously\ convex.$
$from\ \nabla f(x^*)=0,\ we\ have\ x^*=1\ and\ f(x^*)=1$

$(b)$
$step = -[\nabla ^2 f(x)]^{-1}\nabla f(x) = x-x^2
$

$(c)$

$(d)$
$$
\begin{aligned}
y_{k+1}&=\ \mid x_{k+1}-x^*\mid\\
&=\ \mid x_k + x_k - x_k^2 - 1\mid\\
&=\ \mid (x_k-1)^2\mid\\
&=\ y_k^2
\end{aligned}
$$
$By\ induction\ y_k=y_0^{2^k}$
$x_k\rightarrow x^* \Leftrightarrow (y_0)^2< 1\Leftrightarrow \mid x_0-x^*\mid < 1,\ which\ is\ consistent\ with\ results\ in\ (c).$

$(e)$
