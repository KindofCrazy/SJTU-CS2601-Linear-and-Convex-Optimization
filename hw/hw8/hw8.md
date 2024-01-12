# HW8

## 1

$(a)$
$f(\boldsymbol{x})\ is\ obviously\ convex.$
$$
\nabla f(\boldsymbol{x}^*) = \begin{bmatrix}
    e^{x_1+3x_2-0.1}+e^{x_1-3x_2-0.1}-e^{-x_1-0.1} \\
    3e^{x_1+3x_2-0.1}-3e^{x_1-3x_2-0.1}
\end{bmatrix}=\boldsymbol{0}
\Rightarrow \boldsymbol{x}^*=\begin{bmatrix}
    log(\frac{\sqrt{2}}{2}) \\
    0
\end{bmatrix}
$$
$f(\boldsymbol{x}^*)=e^{-0.1}(2e^{\frac{\sqrt{2}}{2}}+e^{-\frac{\sqrt{2}}{2}})
$
