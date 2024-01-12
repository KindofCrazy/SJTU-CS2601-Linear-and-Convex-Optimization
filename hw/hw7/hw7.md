# HW7

## 1

$(a)$

$f(x)\ is\ \lambda_1-smooth\ and\ \lambda_n-strongly\ convex$
$\therefore t\in (0, \frac{2}{\lambda_1})$

$(b)$
$$
\nabla f(\boldsymbol{x}^*)=0\Rightarrow \boldsymbol{Ax}^*=\boldsymbol{b}
$$

$(c)$
$$
\begin{aligned}
\boldsymbol{x}_{k+1}-\boldsymbol{x}^*&=\boldsymbol{x}_k-t(\nabla f(\boldsymbol{x}_k)+\boldsymbol{e}_k)-\boldsymbol{x}^*\\
&=\boldsymbol{x}_k-\boldsymbol{x}^*-t(\boldsymbol{Ax}_k-\boldsymbol{b}+\boldsymbol{e}_k)\\
&=\boldsymbol{x}_k-\boldsymbol{x}^*-t\boldsymbol{A}(\boldsymbol{x}_k-\boldsymbol{x}^*)-t\boldsymbol{e}_k\\
&=(\boldsymbol{I}-t\boldsymbol{A})(\boldsymbol{x}_k-\boldsymbol{x}^*)-t\boldsymbol{e}_k\\
\end{aligned}
$$

$(d)$
$$
\begin{aligned}
\Vert \boldsymbol{x}_{k+1}-\boldsymbol{x}^*\Vert_2&=\Vert (\boldsymbol{I}-t\boldsymbol{A})(\boldsymbol{x}_k-\boldsymbol{x}^*)-t\boldsymbol{e}_k\Vert_2\\
&\leq \Vert (\boldsymbol{I}-t\boldsymbol{A})(\boldsymbol{x}_k-\boldsymbol{x}^*)\Vert_2+\Vert t\boldsymbol{e}_k\Vert_2\\
&\leq (1-\lambda_nt) \Vert\boldsymbol{x}_k-\boldsymbol{x}^*\Vert_2+t\Vert\boldsymbol{e}_k\Vert_2\\
&\leq (1-\lambda_nt) \Vert\boldsymbol{x}_k-\boldsymbol{x}^*\Vert_2+tE\\
\end{aligned}
$$

$(e)$

$$
\begin{aligned}
\Vert\boldsymbol{x}_k-\boldsymbol{x}^*\Vert_2&\leq (1-\lambda_nt)\Vert\boldsymbol{x}_{k-1}-\boldsymbol{x}^*\Vert_2+tE\\
&\leq (1-\lambda_nt)((1-\lambda_nt)\Vert\boldsymbol{x}_{k-2}-\boldsymbol{x}^*\Vert_2+tE)+tE\\
&=(1-\lambda_nt)^2\Vert\boldsymbol{x}_{k-2}-\boldsymbol{x}^*\Vert_2+(1-\lambda_nt)tE+tE\\
&\leq ...\\
&\leq (1-\lambda_nt)^k\Vert\boldsymbol{x}_{0}-\boldsymbol{x}^*\Vert_2+tE\cdot\sum_{i=0}^{k-1}(1-\lambda_nt)^i\\
&=(1-\lambda_nt)^k\Vert\boldsymbol{x}_{0}-\boldsymbol{x}^*\Vert_2+tE\cdot\frac{1-(1-\lambda_nt)^k}{1-(1-\lambda_nt)}\\
&=(1-\lambda_nt)^k\Vert\boldsymbol{x}_{0}-\boldsymbol{x}^*\Vert_2+\frac{1-(1-\lambda_nt)^k}{\lambda_n}E
\end{aligned}
$$

$(f)$

$$
\begin{aligned}
\limsup_{k\rightarrow\infin}\Vert\boldsymbol{x}_k-\boldsymbol{x}^*\Vert_2&\leq \limsup_{k\rightarrow\infin}(1-\lambda_nt)^k\Vert\boldsymbol{x}_{0}-\boldsymbol{x}^*\Vert_2+\frac{1-(1-\lambda_nt)^k}{\lambda_n}E\\
&=\frac{E}{\lambda_n}(1-\lim_{k\rightarrow\infty}(1-\lambda_nt)^k)\\
&=\frac{E}{\lambda_n}
\end{aligned}
$$

## 2

$We\ have\ \forall \boldsymbol{x},\boldsymbol{y}$
$$
\newcommand{\x}{\boldsymbol{x}}
\newcommand{\y}{\boldsymbol{y}}
f(\y)\geq f(\x)+\nabla f(\boldsymbol{x})^T(\boldsymbol{y}-\boldsymbol{x})+\frac{\alpha}{2}\Vert \x-\y\Vert_2\\
g(\y)\leq g(\x)+\nabla g(\boldsymbol{x})^T(\boldsymbol{y}-\boldsymbol{x})+\frac{\beta}{2}\Vert \x-\y\Vert_2
$$
$By\ subtracting$
$$
\newcommand{\x}{\boldsymbol{x}}
\newcommand{\y}{\boldsymbol{y}}
\begin{aligned}
&\quad f(\y)-g(\y)\geq (f(\x)-g(\x))+(\nabla f(\x)-\nabla g(\x))^T(\y-\x)+\frac{\alpha-\beta}{2}\Vert\x-\y\Vert_2\\
\Leftrightarrow & \quad h(\y)\geq h(\x)+\nabla h(\x)^T(\y-\x)+\frac{\alpha-\beta}{2}\Vert\x-\y\Vert_2
\end{aligned}
$$
$When\ \alpha>\beta$
$$
\newcommand{\x}{\boldsymbol{x}}
\newcommand{\y}{\boldsymbol{y}}
h(\y)\geq h(\x)+\nabla h(\x)^T(\y-\x)
$$
$Accoring\ to\ the\ first-order\ condition,\ h(\boldsymbol{x})\ is\ convex.$

## 3

$
\newcommand{\x}{\boldsymbol{x}}
f(\x)=\x^T\begin{bmatrix}
    \frac{1}{2}&\frac{1-\epsilon}{2}\\
    \frac{1-\epsilon}{2}&\frac{1}{2}
\end{bmatrix}\x,\ thus\ \lambda_{max}=\frac{2-\epsilon}{2},\ \lambda_{min}=\frac{\epsilon}{2}
$
$Therefore,\ condition\ number\ \kappa(\boldsymbol{Q})=\frac{2-\epsilon}{\epsilon}.\ When\ \epsilon\rightarrow0,\ condition\ number\ increases\ to\ \infty.$
