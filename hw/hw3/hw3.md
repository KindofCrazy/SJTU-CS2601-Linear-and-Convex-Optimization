# HW3

## 1

$\Rightarrow:$
$\because \sum_{i=0}^mc_ix_i=0\ and \sum_{i=0}^mc_i=0$
$\therefore \sum_{i=1}^mc_i(x_i-x_0)=0$
$\because x_0, x_1, ..., x_m\ are\ affinely\ independent$
$\therefore c_i=0, for\ i =1,2,...,m$
$\therefore c_i=0, for\ i =0,1,2,...,m$

$\Leftarrow:$
$Assume\ \sum_{i=1}^mk_i(x_i-x_0)=0$
$Let\ c_0=-\sum_{i=1}^mk_i, c_i=k_i(i=1,2,...,m)$
$
\sum_{i=0}^mc_ix_i=\sum_{i=1}^mk_i(x_i-x_0)=0\
and\ \sum_{i=0}^mc_i=0
$
$\therefore c_i=k_i=0(i=1,2,...,m)$
$\therefore (x_i-x_0)\ is\ independent\ for\ i=1,2,...,m$
$\therefore x_0,x_1,...,x_m\ is\ affinely\ independent$

## 2

$x,y\in \Delta_{n-1}=\{x\in R^n:x\geq 0, 1^Tx=1\}$
$$
\begin{align}
KL(x||y)&=\sum_{i=1}^nx_ilog\frac{x_i}{y_i}\\
&=-\sum_{i=1}^nx_ilog\frac{y_i}{x_i}\\
&\geq -log(\sum_{i=1}^nx_i\frac{y_i}{x_i})\\
&=-log(\sum_{i=1}^ny_i)\\
&=0
\end{align}
$$

## 3

$\forall \theta\in[0,1],\forall x_1,x_2\in M,i.e.\ \forall x\in S, f(x_1)\leq f(x), f(x_2)\leq f(x)$
$\because S\ is\ convex\ \therefore \theta x_1+(1-\theta)x_2\in S$
$\forall x\in S, f(\theta x_1+(1-\theta)x_2)\leq \theta f(x_1)+(1-\theta)f(x_2)\leq f(x)$
$\therefore \theta x_1+(1-\theta)x_2\in M$
$\therefore M\ is\ convex$

## 4

$Assume\ \theta_1\in(0, \theta_0)\ f(\theta_1x+\mathop{\theta_1}\limits^-y)<\theta_1f(x)+\mathop{\theta_1}\limits^-f(y)$
$$
\begin{align}
f(\theta_0x+(1-\theta_0)y)&=f(\frac{\theta_0-\theta_1}{1-\theta_1}x+\frac{1-\theta_0}{1-\theta_1}(\theta_1x+(1-\theta_1)y))\\
&\leq \frac{\theta_0-\theta_1}{1-\theta_1}f(x)+\frac{1-\theta_0}{1-\theta_1}f(\theta_1x+(1-\theta_1)y)\\
&<\frac{\theta_0-\theta_1}{1-\theta_1}f(x)+\frac{1-\theta_0}{1-\theta_1}(\theta_1f(x)+(1-\theta_1)f(y))\\
&=\theta_0f(x)+(1-\theta_0)f(y)
\end{align}
$$
$\because f(\theta_0x+(1-\theta_0)y)=\theta_0f(x)+(1-\theta_0)f(y)$
$\therefore f(\theta_1x+\mathop{\theta_1}\limits^-y)=\theta_1f(x)+\mathop{\theta_1}\limits^-f(y)$

## 5

(a)
$$
\begin{align}
\forall x\in [a,b]\quad f(x)&=f(\frac{b-x}{b-a}a+\frac{x-a}{b-a}b)\\
&\leq \frac{b-x}{b-a}f(a)+\frac{x-a}{b-a}f(b)\\
\end{align}
$$

(b)
$$
\begin{align}
\forall x\in (a,b)\quad \frac{f(x)-f(a)}{x-a}&\leq \frac{\frac{b-x}{b-a}f(a)+\frac{x-a}{b-a}f(b)-f(a)}{x-a}\\
&=\frac{f(b)-f(a)}{b-a}
\end{align}
$$
$The\ other\ side\ is\ similar.$

(c)
$$
\begin{align}
&\lim_{x\to a^+}\frac{f(x)-f(a)}{x-a}&\leq \lim_{x\to a^+}\frac{f(b)-f(a)}{b-a}\\
\Rightarrow &\quad\quad\quad f^{'}(a)&\leq \frac{f(b)-f(a)}{b-a}
\end{align}
$$
$The\ other\ side\ is\ similar.\ f^{'}\ is\ monotonically\ increasing$

(d)
$\because a<b$
$\therefore f^{'}(a)\leq f^{'}(b)$
$\forall x\in S,\ f^{''}(x)=\lim_{b\to x^+}\frac{f^{'}(b)-f^{'}(x)}{b-x}\geq 0$

## 6

$\textbf{To\ Be\ Solved}$

(a)

$$
\beta = \sup_{a<s<\mu}\frac{f(\mu)-f(s)}{\mu-s}> -\infty
$$
$When\ x=\mu,\ statement\ obviously\ holds.$
$When\ a< x < \mu$
$$
f(x)\geq f(\mu) + \beta(x-\mu)\Leftrightarrow \frac{f(\mu)-f(x)}{\mu-x}\leq \beta
$$
$When\ \mu < x < b$
$$
f(x)\geq f(\mu) + \beta(x-\mu)\Leftrightarrow \frac{f(x)-f(\mu)}{x-\mu}\geq \beta
$$

(b)
$X\ is\ random\ variable\ taking\ values\ in\ (a, b).$
$$
f(X)\geq f(\mu)+\beta(X-\mu)\\
$$
$By\ taking\ expection:$
$$
\mathbb{E}f(X)\geq f(\mu)+\beta(\mathbb{E}X-\mu)=f(\mu)=f(\mathbb{E}X)
$$

## 7

(a)
$Induction\ Basis:\ When\ k=1, holds\ by\ definition$
$Induction\ Step:\ Assume\  When\ k=n, statement\ holds.\ We\ need\ to\ prove\ when\ k=n+1, \ statement\ holds.$
$$
\begin{align}
f(\frac{x_1+x_2+...+x_{2^{k+1}}}{2^{k+1}})&=f(\frac{\frac{x_1+x_2+...+x_{2^k}}{2^k}+\frac{x_{2^{k}+1}+x_{2^k+2}+..x_{2^{k+1}}}{2^k}}{2})\\
&\leq \frac{1}{2}[f(\frac{x_1+x_2+...+x_{2^k}}{2^k})+f(\frac{x_{2^{k}+1}+x_{2^k+2}+..x_{2^{k+1}}}{2^k})]\\
&\leq \frac{1}{2}\{\frac{1}{2^k}[f(x_1)+f(x_2)+...+f(x_{2^{k+1}})]\}\\
&=\frac{1}{2^{k+1}}[f(x_1)+f(x_2)+...+f(x_{2^{k+1}})]
\end{align}
$$
$Therefore\ statement\ is\ true\ for\ k\in\mathbb{N}.$

(b)
$Assume\ 2^{k-1}<n\leq 2^k.\ Let\ x_i=\frac{x_1+...+x_n}{n}\ for\ i=n+1, ..., 2^k\ in\ part\ (a)$
$$
\begin{align}
f(\frac{x_1+x_2+...x_n}{n})&=f(\frac{x_1+x_2+...+x_{2^k}}{2^k})\\
&\leq \frac{1}{2^k}[f(x_1)+f(x_2)+...+f(x_{2^k})]\\
&=\frac{1}{2^k}[f(x_1)+f(x_2)+...+f(x_n)]+\frac{2^k-n}{2^k}f(\frac{x_1+x_2+...+x_n}{n})
\end{align}
$$
$Therefore$
$$
f(\frac{x_1+x_2+...x_n}{n})\leq \frac{1}{n}[f(x_1)+f(x_2)+...+f(x_n)]
$$

(c)

$$
\begin{align}
f(\frac{p}{p+q}x_1+\frac{q}{p+q}x_2)&=f(\frac{\sum_{i=1}^px_1+\sum_{i=1}^qx_2}{p+q})\\
&\leq \frac{p}{p+q}f(x_1)+\frac{q}{p+q}f(x_2)
\end{align}
$$

$For\ rational\ \theta\in \mathbb{Q}\ \cap (0,1),\ \theta=\frac{p}{p+q}\ for\ some\ p\ and\ q\in \mathbb{N}$

$\textbf{Supplementary\ proof:}$
$Assume\ \theta=\frac{m}{n}\in \mathbb{Q}\ \cap (0,1), therefore\ n>m>0.$
$Let\ p=m,\ q=n-m.\ Thus\ \theta = \frac{p}{p+q}.$

$\textbf{Another\ proof}:
\frac{n}{m}\in \mathbb{Q}>1, thus\ \frac{n}{m}-1\in \mathbb{Q}>0.\ Assume\ \frac{n}{m}-1=\frac{p}{q},\ thus\ \frac{m}{n}=\frac{p}{p+q}.$

(d)
$When\ \theta=0\ or\ \theta=1, statement\ holds\ obviously.$
$For\ raional\ \theta\in (0,1), (c)\ proves$
$For\ irrational\ \theta\in (0,1), \ let\ \{\theta_n\}\ be\ a\ sequence\ of\ irrational\ numbers\ in\ \mathbb{Q}\ \cap (0,1)\ such\ that\ \theta_n\to \theta.
$
$$f(\theta_n x_1+(1-\theta_n)x_2)\leq \theta_nf(x_1)+(1-\theta_n)f(x_2)$$
$By\ taking\ limit\ on\ both\ sides\ of\ the\ inequality,\ conclude\ that$
$$f(\theta x_1+(1-\theta)x_2)\leq \theta f(x_1)+(1-\theta)f(x_2)$$
