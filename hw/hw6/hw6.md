# HW6

## 1

$(a)$
$\nabla f(\boldsymbol{x})=\boldsymbol{Qx}=
\begin{bmatrix}
    x_1 \\
    \gamma x_2 \\
\end{bmatrix}
$
$$
\begin{aligned}
\Vert \nabla f(\boldsymbol{x}) -\nabla f(\boldsymbol{y})\Vert &=((x_1-y_1)^2+\gamma^2(x_2-y_2)^2)^{\frac{1}{2}} \\
&\leq max\{1, \gamma\}\Vert \boldsymbol{x}-\boldsymbol{y}\Vert
\end{aligned}
$$
$Thus\ the\ smallest\ L\ is \ max\{1, \gamma\}.$

$(b)$

$See\ figures$

## 2

$See\ figures$

## 3

$(a)$ $\textrm{dom}f=\mathbb{R^3}\ is\ convex.$
$Assume\ h(x)=-log(\frac{1}{1+e^x}),\ h^{''}(x)=\frac{e^x}{(1+e^x)^2}\leq 0, thus\ h(x)\ is\ concave.$
$\therefore h(-\boldsymbol{x^T\theta})=-log(\sigma_{\boldsymbol{\theta}}(\boldsymbol{x_i}))\ is\ convex\ in\ \theta.$
$Similarily\ -log(1-\sigma_{\boldsymbol{\theta}}(\boldsymbol{x_i}))\ is\ convex\ in\ \theta.$
$\because y^i,\ 1-y^i\geq 0$
$\therefore f(\boldsymbol{\theta})=\sum_{i=1}^Ny^i(-log(\sigma_{\boldsymbol{\theta}}(\boldsymbol{x_i})))+(1-y^i)(-log(1-\sigma_{\boldsymbol{\theta}}(\boldsymbol{x_i})))\ is\ convex.$

$(b)$
$$
\begin{aligned}
\nabla f(\boldsymbol{\theta})&=-\sum_{i=1}^N[y^i\frac{1}{\sigma_{\boldsymbol{\theta}}(\boldsymbol{x_i})}\boldsymbol{x}^i\sigma_{\boldsymbol{\theta}}(\boldsymbol{x}^i)(1-\sigma_{\boldsymbol{\theta}}(\boldsymbol{x}^i))+(1-y^i)\frac{1}{1-\sigma_{\boldsymbol{\theta}}(\boldsymbol{x}^i)}\boldsymbol{x}^i\sigma_{\boldsymbol{\theta}}(\boldsymbol{x}^i)(1-\sigma_{\boldsymbol{\theta}}(\boldsymbol{x}^i))]\\
&=-\sum_{i=1}^N(y^i-\sigma_{\boldsymbol{\theta}}(\boldsymbol{x}^i))\boldsymbol{x}^i\\
&=\sum_{i=1}^N(\sigma_{\boldsymbol{\theta}}(\boldsymbol{x}^i)-y^i)\boldsymbol{x}^i
\end{aligned}
$$
