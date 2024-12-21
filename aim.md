矩阵理论1

# <font color=purple>特殊矩阵</font>

## <font color=blue>H 阵</font>



`Hermite matrix`

- <mark>定义</mark>
  - <font color=red>$A=A^H \in C^{n\times n}$</font>
- <mark>判定</mark>
  A是Hermite矩阵的充要条件
  - ①存在酉矩阵 $U$ 使得 <font color=red>$U^HAU=\Lambda= \mathbf{diag}(\lambda_1,\cdots,\lambda_n)$</font>
     均为实数
  - ②对任意方阵$S$ ，$S^HAS$ 为Hermite矩阵
  - 如果 A , B 是Hermite阵，则$AB$ 是Hermite矩阵的充要条件是$AB=BA$
- <mark>性质</mark>
  - 主对角线元素`对角元`为实数
    - $A=\begin{pmatrix}a_{11}&&&*\\&a_{22}&&\\&&\ddots&\\*&&&a_{nn}\end{pmatrix}A^H=\begin{pmatrix}\overline{a_{11}}&&&*\\&\overline{a_{22}}&&\\&&\ddots&\\*&&&\overline{a_{nn}}\end{pmatrix}$
  - $A$ 有 $n$ 个互相正交的特征向量，即 $X_1\bot X_2\bot...\bot X_n$
     的不同特征值所对应的特征向量是相互正交的
    - proof
      - ![](https://api2.mubu.com/v3/document_image/21954114_47c562e0-65dd-4f49-de96-01d9083a624b.png)
  - $a_{i,j}=\overline{a_{j,i}}$
  - 任何<mark>实对称矩阵</mark>是`Hermite`矩阵
  - 每个H阵 A <mark>优相似于对角阵</mark>
    - 存在优阵 $Q\\$ 使 $Q^{-1}AQ=Q^HAQ=\Lambda=\begin{pmatrix}\lambda_1&&\\&\ddots&\\&&\lambda_n\end{pmatrix}\\ A=Q\Lambda Q^{-1}=Q\Lambda Q^H$，且 $\lambda(A)\in R$
      - proof
        - ![](https://api2.mubu.com/v3/document_image/21954114_75076d8d-7ce5-4964-bb3f-bf6dea24e641.png)
  - <mark>特征根都是实数</mark>，$\{\lambda_1,\cdots,\lambda_n\}\in R$
    - $\begin{aligned}&\text{由特商公式}\lambda=\frac{X^HAX}{|X|^2}\text{,其中}X\neq0\text{,}\lambda\text{的特征向量} \\&\text{其中}|X|\geq0\text{,为实数}. \\&\therefore\text{若}\lambda\text{为实数,即证}X^HAX\text{为实数} \\&\text{已知}X^HAX\text{为一维数字,则只需证明}（X^HAX)^H=X^HAX\text{即可}, \\&\text{已知}A=A^H\text{为}Hermite\text{矩阵,}（X^HAX)^H=X^HA^HX=X^HAX\in R \end{aligned}$ proof
  - 对正整数 $k$，$A^k$ 也是 $H$ 阵
  - 若 $A$ 可逆，$A^{-1}$ 也是 $H$ 阵
  - 对实数 $k , p$ ，$k A + p B$ 也是Hermite矩阵
    A , B为n 阶Hermite矩阵
- <mark>乘积形式的H阵性质</mark>
  - 对一切矩阵$A=A_{n\times p}$ 且 $n\geq p$ ，$A^HA$与$AA^H$都是`Hermite`阵
    - proof
      - ![](https://api2.mubu.com/v3/document_image/21954114_7ba61f5c-9ffc-4ab6-d3b2-c7adaff2516f.png)
  - $AA^H$ 矩阵的迹
    - $A_{n\times p}=\begin{pmatrix}a_{11}&\cdots&a_{1p}\\\vdots&\ddots&\vdots\\a_{n1}&\cdots&a_{np}\end{pmatrix}\in C^{n\times p}\\ A_{p\times n}^H=\begin{pmatrix}\overline{a_{11}}&\cdots&\overline{a_{n1}}\\\vdots&\ddots&\vdots\\\overline{a_{1p}}&\cdots&\overline{a_{np}}\end{pmatrix}\in C^{p\times n}$
    - $\displaystyle tr(A^HA)=tr(AA^H)=\sum\limits_{i=1,j=1}^n{|a_{ij}|^2}$
    - 推论
      - $tr(AB^H)=tr(B^HA)=\sum a_{ij}\overline{b_{ij}}$
  - $A^HA$ 与 $AA^H$只相差 $n-p$ 个 0 根
    - proof
      - ![](https://api2.mubu.com/v3/document_image/21954114_456a6946-33e1-4c54-8b93-5635b7dc5b50.png)
  - $A^HA$ 与 $AA^H$ 是<mark>半正定阵</mark>
    - proof
      - ![](https://api2.mubu.com/v3/document_image/21954114_6c98f7d6-2751-4613-ee5f-1247e7978663.png)
  - $r(AA^H)=r(A^HA)=r(A)=r(A^H)$
    - proof 1
      - ![](https://api2.mubu.com/v3/document_image/21954114_625102e6-be5d-4ae6-b7cf-4d8668b4e94d.png)
    - proof 2——只需证$A^HAX= 0$ 的解也是 $AX=0$ 的解
      - ![](https://api2.mubu.com/v3/document_image/21954114_f0969394-dba4-4830-a01a-61a838edf46d.png)
## <font color=blue>二次型、正定阵</font>



参考资料 [csdn](https://blog.csdn.net/hzf0701/article/details/134824086)

- <font color=codespan>`Hermite`</font><font color=green>二次型定义</font>
  - 令 $A^H=A\in C^{n\times n}$，$X=\begin{pmatrix}x_1\\x_2\\\vdots\\v_n \end{pmatrix}$
  - 称 $X^HAX=(\overline{x_1},\overline{x_2},\cdots,\overline{x_n}) A\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix}\\$为矩阵 $A$ 产生的二次型，记作 $f(x)=X^HAX$
- <font color=green>正定二次型与正定阵定义</font>
  - 若$A^H=A$ ，对一切$X\neq0$ ，有$X^HAX>0$ ，则$f(x)=X^HAX$为<mark>正定二次型</mark>，$A$为<mark>正定阵</mark>，记为 $A>0$
  - 若$A^H=A$ ，对一切$X\neq0$ ，有$X^HAX\geq0$ ，则$f(x)=X^HAX$为<mark>半正定二次型</mark>，A为<mark>半正定阵</mark>，记为 $A\geq0$
  - all
    - ![](https://api2.mubu.com/v3/document_image/21954114_ed06eb89-6c17-4b0b-9559-3fcfdea2cdf1.png)
- <font color=green>判定 </font><font color=green>$n$</font><font color=green> 阶Hermite矩阵 </font><font color=green>$A$</font><font color=green> 正定</font>
  - all
    - ![](https://api2.mubu.com/v3/document_image/21954114_9ac3669d-614f-407d-f362-05549e35cb18.png)
- <font color=green>正定阵定理</font>
  - $A>0\Longleftrightarrow A$为Hermite阵，且$\lambda_1,\lambda_2,\cdots,\lambda_n>0\\$ $A\geq0\iff A$为Hermite阵，且$\lambda_1,\lambda_2,\cdots,\lambda_n\geq0$
    - proof
      - ![](https://api2.mubu.com/v3/document_image/21954114_e18ba551-1d01-4828-9864-b892facf5c7c.png)
  - 单位阵是正定阵
  - 正定阵间必合同
    - $A >0 \iff A \triangleq \Lambda$
    - $\Lambda \triangleq I$
    - 若 $A,B$ 为同阶正定阵，则 $A \triangleq B$
    - proof
      - ![](https://api2.mubu.com/v3/document_image/21954114_dff8a744-3754-48b0-dc7d-d5fc47a3d3f0.png)
## <font color=blue>斜H阵</font>



`Skew-Hermit`

- $A^H=-A$
- <mark>性质</mark>
  - 对角元为纯虚数
  - 若 $B$ 是 `skew-Hermit` $\rightarrow$ $iB$ 与 $\displaystyle \frac{B}{i}$ 都是`Hermit`
  - 若 $A$ 是 `Hermit` $\rightarrow$ $iA$ 与 $\displaystyle \frac{A}{i}$ 都是`Skew-Hermit`
  - $A$ 是 `Hermit` $\Leftrightarrow$ $iA$ 是 `Skew-Hermit`
## <font color=blue>正交阵</font>



- $A^TA=AA^T=I$
- <mark>性质</mark>
  - 正交矩阵的任一行（列）同时乘以−1时，得到的新矩阵仍为正交矩阵
  - 正交矩阵的行列式必为 ±1
## <font color=blue>优阵（U阵）</font>



- 如果 $A=(\alpha_1,\alpha_2,\cdots,\alpha_n)_{n\times n}$ 是且$|\alpha_1|=|\alpha_2|=\cdots=|\alpha_p|=1$，那么$A$ 是一个优阵
- <mark>判定</mark>
  - $A=(\alpha_1,\alpha_2,\cdots,\alpha_n)_{n\times n}$是U阵 $\iff\\$ $|\alpha_1|=|\alpha_2|=\cdots=|\alpha_p|=1$ 且 $\alpha_1\perp\alpha_2\perp\cdots\perp\alpha_n$
  - <font color=red>$A=A_{n,n} 是 U阵 \\ \Leftrightarrow A^{H} A=I_{\mathrm{n}} \\ \Leftrightarrow A^{-1}=A^{H} \\ \Leftrightarrow AA^{H}=I_{\mathrm{n}}$</font>
- <mark>性质</mark>
  如果 A 是U阵
  - 如果 $A_{n,n}和B_{n,n}$ 是U阵 $\Rightarrow$ $AB$是U阵
  - $A 是U，且X_1\bot X_2\cdots\bot X_p \Rightarrow$ $AX_1\bot AX_2\cdots\bot AX_p$
  - $k=\pm1,kA=(k\alpha_1,k\alpha_2,\cdots,k\alpha_n)\text{ 为优阵}$
  - $B=(\beta_1,\beta_2,\cdots,\beta_n)$为优阵，其中$\beta\text{ 组为 }\alpha\text{ 组的重排}$
  - $|Ax|^2=|x|^2$
    - ![](https://api2.mubu.com/v3/document_image/ab81598e-2cf4-420a-be0e-01a78666e299-21954114.jpg)
  - $x\bot y\Rightarrow Ax\bot Ay$
    - ![](https://api2.mubu.com/v3/document_image/c235ea90-ad61-4a9c-98c1-0b60ca48e31e-21954114.jpg)
  - $(Ax,Ay)=(x,y)$
- <mark>拓展性质</mark>
  - U阵的任一行（列）同时乘以模为1的任何数后，得到的新矩阵仍为U阵
## <font color=blue>正规阵</font>



- 方阵 $A$ 满足 $A^HA=AA^H$
  正规阵必为方阵
- <font color=green>判定</font>
  - <font color=blue>H 阵 </font>、<font color=blue>斜H阵</font>、<font color=blue>正交阵</font>、（包含实正交阵）都是正规阵
  - 对角阵一定是正规阵
  - 实对称与实反对称阵都正规
  - 复方阵A是正规矩阵 当且仅当 A优相似于对角阵
- <font color=green>性质</font>
  - 若$A$正规，则$kA＋cI$正规
  - 若$A$正规，则$A$与$A^H$必有相同特征向量
    - 即若$A$正规，且$AX＝cX$，则$A^HX＝\bar{c}X$
  - 若$A$正规，则$Q^HAQ$也正规，其中$Q$为优阵（$QQ^H＝I$）
    正规阵的优相似必正规
  - 若$A$正规，则任意多项式$f(A)＝λ_ 0 I+λ _1 A+λ _2 A ^2 +⋯+λ_nA^K$也正规
    多项正规定理——正规阵的多项式也正规
  - 正规阵A恰有n个正交的特征向量
  - 正规矩阵酉相似于对角矩阵
- 严格三角阵（非对角形）一定不是正规阵
- <font color=green>引理</font>—$\text{若分块阵 }A=\begin{pmatrix}B&C\\0&D\end{pmatrix}\text{正规，则 }C=0\text{，且 }B,D\text{ 都正规，即 }A=\begin{pmatrix}B&0\\0&D\end{pmatrix}$
## <font color=blue>λ矩阵</font>



- <font color=green>定义</font>
  - 以 λ多项式 为元素的矩阵称为λ矩阵，记为`A(λ)`
    - <mark>$A(λ)=[a_{ij}(λ)]_{m×n}$</mark>
- <font color=bold>λ矩阵的秩</font>
  - 矩阵A(λ)中<u>非零子式的最高阶数r</u> 定义为A(λ)的秩，记为`rank(A(λ))=r`
  - 例子
    - ![](https://api2.mubu.com/v3/document_image/21954114_81336d7f-e5a5-482e-b7fb-c838996a23b9.png)
- <font color=bold>λ矩阵相抵</font>
  - <mark>定义</mark>
    - 若λ矩阵A(λ)经过<mark>有限次初等变换</mark>化为B(λ)，则称A(λ)与B(λ)<font color=red>相抵</font>
    - $A(λ)≅B(λ)$
  - <mark>性质</mark>
    - λ矩阵相抵则其秩相同，反之则不然
    - 相抵的λ矩阵具有相同的秩和相同的各阶行列式因子
    - λ矩阵A(λ)与B(λ)相抵 的<mark>充要条件</mark>
      - or 完全一致的<font color=green>不变因子</font>
      - or 具有<u>相同的各阶行列式因子</u>
      - or 完全一致的<font color=green>初等因子</font>，且 <font color=green>$rank\big (A(λ)\big)=rank\big(B(λ)\big)$</font>
    - 复方阵A和B相似当且仅当它们的特征矩阵相抵
      - - ![](https://api2.mubu.com/v3/document_image/21954114_f94dc556-0da1-4575-f465-23e777e6293a.png)
        - ![](https://api2.mubu.com/v3/document_image/21954114_1f7d7b7c-a585-4c38-d907-eee79c2df57d.png)
  - <mark>例子</mark>
    - ![](https://api2.mubu.com/v3/document_image/21954114_b9e865ad-43ac-4bd5-8818-6bd1f56e1db2.png)
- <font color=bold>λ矩阵的逆矩阵</font>
  - 设 $A(λ)$ 是 $n$ 阶 $λ$ 方阵，若存在 $n$ 阶$λ$方阵$B(λ)$满足<font color=red>$A(λ)B(λ)=B(λ)A(λ)=I$</font> 则称λ矩阵A(λ)是可逆的,并称B(λ)为A(λ)的逆矩阵,记作$A(λ)^{−1}$
  - λ方阵A(λ)可逆的<u>充分必要条件</u>是其行列式$|A(λ)|$为非零常数
    - ![](https://api2.mubu.com/v3/document_image/21954114_69ad8dda-9bc4-4c2c-f117-29e71fc5ea01.png)
- <font color=green>Smith标准形</font>
  - <mark>定义</mark>
    - 设 $λ$ 矩阵 $A(λ)$ 的秩为 $r$
    - 此标准形为A(λ)的Smith标准形
      - ![](https://api2.mubu.com/v3/document_image/21954114_7fd792fb-19e3-434c-b461-ae9f0d62d23c.png)
    - $d_i(λ)$ 是首1多项式，且 $d_i(λ)|d_{i+1}(λ)$
  - <mark>tips</mark>
    - A(λ)不一定是方阵，故Smith标准形不一定是对角阵
    - Smith标准形与行列式因子之间的关系
      - - ![](https://api2.mubu.com/v3/document_image/21954114_a79db914-b684-4b47-9e3d-cfb939b426b8.png)
    - λ矩阵的Smith标准形是唯一的
  - <mark>例子</mark>
    - - ![](https://api2.mubu.com/v3/document_image/21954114_fb2526dc-56ff-4daf-fe73-d4cbb3db366f.png)
      - ![](https://api2.mubu.com/v3/document_image/21954114_42b71ee8-c987-4445-e010-e939aab1110a.png)
- <font color=green>不变因子</font>
  - <mark>定义</mark>
    - 在 λ 矩阵 A(λ) 的Smith标准形中
    - <font color=red>$d_1(λ),⋯,d_{r}(λ)$</font> 由 A(λ) 唯一确定的，称为A(λ)的不变因子
- <font color=green>初等因子</font>
  - <mark>定义</mark>
    - ![](https://api2.mubu.com/v3/document_image/21954114_671dda90-1b75-43c1-9d17-b2bf7da7a51e.png)
  - <mark>例子</mark>
    - ![](https://api2.mubu.com/v3/document_image/21954114_a4c76995-c920-41d2-f498-607c2d571145.png)
  - <mark>tips</mark>
    - 初等变换不改变A(λ)的初等因子
    - 设λ矩阵A(λ)为对角块矩阵
      即
      - 则 $A_1(λ),⋯,A_s(λ)$ 初等因子的全体就是$A(λ)$ 的全部初等因子
- <font color=green>tips</font>
  - 数字矩阵是特殊的λ矩阵
  - 复方阵A的特征矩阵 $λI−A$ 是λ矩阵
    - $λI−A$ 总是满秩的
  - <font color=red>λ方阵A(λ)</font><font color=bold>可逆</font><font color=red>的</font><u><font color=underline>充分必要条件</font></u><font color=red>是其</font><font color=bold>行列式</font><font color=bold>$|A(λ)|$</font><font color=bold>为非零常数</font>
    - - ![](https://api2.mubu.com/v3/document_image/21954114_9995b351-7c07-4d7f-85ff-7e77272a483a.png)
  - 在求λ矩阵的Smith标准形、不变因子或初等因子时
    - 可先将λ矩阵作初等变换，使得变换后的矩阵为对角（块）矩阵
    - 利用定理求出λ矩阵的初等因子，进而求出Smith标准形和不变因子
      设λ矩阵A(λ)为对角块矩阵（定理）
## <font color=blue>度量矩阵</font>



`Gram Martrix`

- <font color=green>定义</font>
  - 设$ϵ_1,⋯,ϵ_n$是内积空间 $V$ 中的一组基，称n阶矩阵A 为$V$ 关于基 $ϵ_1,⋯,ϵ_n$ 的度量矩阵
    - ![](https://api2.mubu.com/v3/document_image/21954114_376d9da9-7e0c-4514-dda6-8c28ae613170.png)
  - 记为 <font color=red>$G(ϵ_1,⋯,ϵ_n)$</font>
- <font color=green>tips</font>
  - 内积空间中内积与度量矩阵是一一对应的
  - <font color=red>$(x,y)=η^HA^Hξ$</font>
    - 设 $ϵ_1,⋯,ϵ_n$ 是内积空间V的一组基，则 $∀x,y∈V$,有
      - ![](https://api2.mubu.com/v3/document_image/21954114_d1334d12-5a51-43f6-9053-0b6c515803cf.png)
- <font color=green>性质</font>
  设  和 均为内积空间  的度量矩阵
  - $G(ε_1,⋯,ε_n)$ 和 $G(ϵ_1,⋯,ϵ_n)$ 是正定Hermite矩阵
  - $G(ε_1,⋯,ε_n)$ 和 $G(ϵ_1,⋯,ϵ_n)$ 合同
    - 即存在非奇异矩阵（可逆矩阵） $P$ 使得
    - $P^HG(ε_1,⋯,ε_n)P=G(ϵ_1,⋯,ϵ_n)$
    - $P$ 是由基 $ε_1,⋯,ε_n$ 到基$ϵ_1,⋯,ϵ_n$ 的过渡矩阵
## <font color=blue>Householder矩阵</font>



- <font color=green>定义</font>
  - 设 $w∈ℂ^n$ 是单位向量
  - $H(w)=I−2ww^H$
- <font color=green>性质</font>
  - $\big(H(w)\big)^H=H(w)=\big(H(w)\big)^{−1}$
  - $|H(w)|=−1$
    特征值 n-1个1， 1个 -1
  - 设 $x, y∈ℂ^n$ 且$x≠y$，则存在单位向量 $w$ 使得$H(w)x=y$ 的充分必要条件是
    - $x^Hx=y^Hy\quad,x^Hy=y^Hx$
    - 此时可取 $\displaystyle w=\frac{e^{iθ}(x−y)}{‖x−y‖}$
      其中θ为任一实数，实际求就取0
## <font color=blue>奇异矩阵</font>



- $|A|=0$
- 没有逆矩阵
## <font color=blue>单纯阵</font>



- <mark>定义</mark>
  - - ![](https://api2.mubu.com/v3/document_image/21954114_58dbab2b-4db5-43b3-cc32-4eb97fa32c61.png)
- <mark>性质</mark>
  - 方阵A是单纯矩阵的充分必要条件
    - or $A$的特征矩阵 $λI−A$的<font color=green>初等因子</font>是一次的
    - or $A$的特征矩阵 $λI−A$ 的<font color=green>不变因子</font>无重根
## <font color=blue>幂零阵、幂等阵</font>



- <font color=green>幂零阵</font>
  - $A^k=0$
  - 幂零阵的全体特征根为0
- <font color=green>幂等阵</font>
  - <mark>定义</mark>
    - $A∈ℂ^{n×n}$
    - $A^2=A$
  - <mark>性质</mark>
    A为幂等阵
    - <font color=red>$A^H$</font>，<font color=red>$A^∗$</font> 和 <font color=red>$I−A$</font>都是幂等矩阵
    - A 为单纯阵且相似于对角阵
      - ![](https://api2.mubu.com/v3/document_image/21954114_46743dd0-8e84-40e1-c29b-1ccc0b0b6490.png)
    - $tr(A)=r$
      - - ![](https://api2.mubu.com/v3/document_image/21954114_7bb21389-c221-43ea-f133-d6ce87749424.png)
    - $N(A)=R(I-A)$
      充要条件
    - $\mathbb C^n=N(A) \dot{+}R(A)$
    - $\mathbb C^n=N(A) \dot{+} N(A-I)$

# <font color=purple>重要概念</font>

## <font color=blue>共轭</font><font color=codespan>Conjugate</font>



- 对<mark>复数</mark> $w=a+ib$
  - $\overline{w}=\overline{a+bi}=a-bi$
- <mark>矩阵的共轭</mark>——矩阵内每个元素取共轭
  - $\overline{A}=(\overline{a_{i,j}})$
- <font color=bold>性质</font>
  - <mark>实矩阵</mark>
    - $\overline{A}=(\overline{a_{i,j}})=(a_{i,j})=A$
  - $\text{对于任意 } A=A_{m\times n}\in\mathbb{C}^{m,n}, B=B_{m\times p}\in\mathbb{C}^{n,p}$
    - $\overline{(AB)}=(\overline{A})(\overline{B})\quad$
## <font color=blue>共轭转置=转置共轭</font>



- $A^H=\overline{A}^T=\overline{A^T}$
- <mark>性质</mark>
  - ${(A^H)}^H=A$
  - $(A+B)^H=A^H+B^H$
  - $(kA)^H=\overline{k}(A^H)$
     （复数）
  - $(ABC)^H=C^HB^HA^H$
## <font color=blue>矩阵的模/范数</font>



- $||A||=\sqrt{\sum|a_{i,j}|^{2}}$
## <font color=blue>向量的模</font>



- $|| X||=\sqrt{(X,X)}=\sqrt{\left|x_1\right|^2+\left|x_2\right|^2+\cdots+\left|x_n\right|^2}\geq0$
- <font color=green>性质</font>
   和 
  - - ![](https://api2.mubu.com/v3/document_image/21954114_87832f43-354c-4aef-d98c-472cddd2fdf0.png)
    - ![](https://api2.mubu.com/v3/document_image/21954114_5d8b4113-7b63-4f91-8308-063542f33ccf.png)
## <font color=blue>迹</font>



- $tr(A)=a_{11}+\ldots+a_{nn}$
- <mark>模平方公式</mark>
  - $tr(A^{H}A)=tr(AA^H)=\sum|a_{i,j}|^{2}={||A||}^2$
    - $\begin{aligned}tr(AA^{H})&=tr[(A^{H})^{H}A^{H}]\\&=||A^{H}||^{2}\\&=\sum|\overline{a_{ij}}|^{2}\\&=||A||^{2}\end{aligned}$
  - 推导前提——<mark>列向量的模平方公式</mark>
    - 对于一个列向量$X$—— $X^HX={\|X\|}^2$
    - $\mathrm{tr}(X^HX)=\mathrm{tr}(XX^H)=\left|x_1\right|^2+\left|x_2\right|^2+\cdots+\left|x_n\right|^2=\sum\left|x_j\right|^2\overset{\text{记为}}{\operatorname*{=}}|\mathbf{X}|^2$
  - <font color=red>推广公式</font>
    - 已知 $A=(a_{ij})_{m\times n}、B=(b_{ij})_{m\times n} \in C^{m\times n}$ 则
      - $tr(AB^H)=tr(B^HA)=\sum a_{ij}\overline{b_{ij}}$
      - $tr(AB^T)=tr(B^TA)=\sum a_{i,j}b_{i,j}$
      - $\mathrm{tr}(XY^{H})=\mathrm{tr}(Y^{H}X)=Y^{H}X=x_{1}\overline{y}_{1}+\cdots+x_{n}\overline{y}_{n}$
        
        - - ![](https://api2.mubu.com/v3/document_image/6cdb49a6-ac88-4312-9e5e-8107fbe14821-21954114.jpg)
        - - ![](https://api2.mubu.com/v3/document_image/ab05e461-6d2a-4a0e-84c4-f35e5a0c8cbc-21954114.jpg)
## <font color=blue>全体特征根</font>



- $\lambda(A)=\{\lambda_1,\ldots,\lambda_n\}$
## <font color=blue>特征值</font>



- 设矩阵<font color=red>$A∈ℂ^{n×n}$</font>的 $n$ 个特征值为 <font color=red>$λ_1,⋯,λ_n$</font>
  - 则矩阵<font color=red>$A^m$</font> 的n个特征值为 <font color=red>$λ_1^m,⋯,λ_n^m$</font>
- 设矩阵<mark>$A∈ℂ^{n×n}$</mark>的 n 个特征值为<mark>$λ_1,⋯,λ_n$</mark>，<mark>$φ(λ)$</mark>为任一多项式
  - 则矩阵多项式<mark>$φ(A)$</mark>的n个特征值为<mark>$φ(λ_1),⋯,φ(λ_n)$</mark>
- [矩阵分析：特征值，相似度对角化，Jordan标准形_jordan标准型和特征值的关系-CSDN博客](https://blog.csdn.net/qq_42192693/article/details/122248940)
## <font color=blue>右逆、左逆</font>



- A有右逆 的充要条件
  即存在矩阵B使得
  - A为行满秩矩阵
- A有左逆 的充要条件
  即存在矩阵B使得
  - A为列满秩矩阵
## <font color=blue>内积</font><font color=codespan>Inner product</font>



- <font color=blue>定义在 </font><font color=blue>$C^n$</font><font color=blue>（列） 上的内积</font>
  与 都是  上的列向量
  - <mark>$X$</mark><mark>与</mark><mark>$Y$</mark><mark>的标准内积</mark>
    - $(X,Y)=Y^HX=\mathrm{tr}(XY^H)=x_1 \overline{y_1}+\cdots+x_n \overline{y_n}$ 类型对比
    - $YX^H=(Y,X)=\overline{(X,Y)}$
  - <mark>特例</mark>
    - $(X,X)=\mathrm{tr}(XX^H)=X^HX=x_1\overline{x_1}+\cdots+x_n\overline{x_n}=\mid x_1\mid^2+\cdots+\mid x_n\mid^2=\mid X\mid^2$
  - <mark>特性</mark>
    - $\mid X\mid^2=(X,X)=\mathrm{tr}(XX^H)=\mathrm{tr}(X^HX)=X^HX=\mid X\mid^2$
    - $Y^HX=(X,Y) \\$ $X^HY=(Y,X)=\overline{(X,Y)}$
    - $\mid kX\mid=\mid k\parallel X\mid\\ \mid\frac{X}{k}\mid=\frac{\mid X\mid}{\mid k\mid},(k\neq0);\quad\\ \mid X\pm Y\mid\leq\mid X\mid+\mid Y\mid.$
      模长性质
    - 如果 $X \ne 0$ 则 $\frac{X}{|X|}$ 是单位向量
      单位化公式
  - <mark>内积性质</mark>
    - $(X,X)\ge 0$
    - $(Y,X)=\overline{(X,Y)}$
    - $(kX,Y)=k(X,Y)\\ (X,kY)=\overline{k}(X,Y)$
    - $(X+Y,W)=(X,W)+(Y,W),\\(W,X+Y)=(W,X)+(W,Y)$
    - $| (X,Y) |^{2}\leq(X,X)(Y,Y)\\ \mathrm{i.e.} | (X,Y) |\leq| X |\cdot| Y|$
- <font color=blue>$C^{1\times n}$</font><font color=blue> （行） 内积公式</font>
  - $（X,Y)=XY^H$ 类型对比
- <font color=blue>定义在 </font><font color=blue>$C^{m,n}$</font><font color=blue>（复矩阵空间）上的内积</font>
  - <mark>定义</mark>
    - $\begin{aligned}(A,B)&\triangleq tr(B^HA)=tr(A^HB)=\sum a_{ij}\overline{b_{ij}} ,A,B\in C^{m,n}\\(A,A)&\triangleq tr(A^HA)=tr(AA^H)=\sum a_{ij}\overline{a_{ij}} =\sum|a_{ij} |^2\end{aligned}$
  - <mark>特性</mark>
    - $(A,A)=tr(AA^H)=\sum\Bigl|a_{ij}\Bigr|^2\geq0$
    - $(B,A)=\overline{(A,B)}$
    - $(kA,B)=k(A,B)$
    - $(A,kB)=\overline{k}(A,B), k\in\mathbb{C}$
    - $(A+B,D)=(A,D)+(B,D)$
    - $(D,A+B)=(D,A)+(D,B)$
  - <mark>性质</mark>
    - $|(A,B)|^2\le(A,A)(B,B)，\text{即}|(A,B)|\le\|A\|\cdot\|B\|$
  - <mark>内积形式（列分块）</mark>
    - $\begin{aligned}A&=\begin{pmatrix}a_{11}&\cdots&a_{1p}\\\vdots&\ddots&\vdots\\a_{n1}&\cdots&a_{np}\end{pmatrix}\in C^{n\times p}\\&=(\alpha_1,\cdots,\alpha_p),\text{其中}\alpha_i\text{为}n\text{维列向量}(n\times1\text{阶矩阵})\end{aligned}$
    - $\begin{aligned}A^{H}& =\begin{pmatrix}\overline{a_{11}}&&\cdots&&\overline{a_{n1}}\\\vdots&&\ddots&&\vdots\\\overline{a_{1p}}&&\cdots&&\overline{a_{np}}\end{pmatrix} \in C^{p\times n} \\&=\begin{pmatrix}\overline{\alpha_1}^T\\\vdots\\\overline{\alpha_p}^T\end{pmatrix}\text{,其中}\overline{\alpha_1}^T\text{是}n\text{维行向量}1\times n\text{阶矩阵})\end{aligned}$
    - $\begin{aligned}A^{H}A& =\begin{pmatrix}\overline{\alpha_1}^T\\\vdots\\\overline{\alpha_p}^T\end{pmatrix}(\alpha_1,\cdots,\alpha_p) \\&=\begin{pmatrix}\overline{\alpha_1}^T\alpha_1&&\overline{\alpha_1}^T\alpha_2&&\cdots&\overline{\alpha_1}^T\alpha_p\\\overline{\alpha_2}^T\alpha_1&&\overline{\alpha_2}^T\alpha_2&&\cdots&\overline{\alpha_2}^T\alpha_p\\\vdots&&\vdots&&\ddots&\vdots\\\overline{\alpha_p}^T\alpha_1&&\overline{\alpha_p}^T\alpha_2&&\cdots&\overline{\alpha_p}^T\alpha_p\end{pmatrix} \\&=\begin{pmatrix}(\alpha_1,\alpha_1)&&(\alpha_2,\alpha_1)&&\cdots&&(\alpha_p,\alpha_1)\\(\alpha_1,\alpha_2)&&(\alpha_2,\alpha_2)&&\cdots&&\alpha_p,\alpha_2)\\\vdots&&\vdots&&\ddots&&\vdots\\(\alpha_1,\alpha_p)&&(\alpha_2,\alpha_p)&&\cdots&&\alpha_p,\alpha_p)\end{pmatrix} \\&=\begin{pmatrix}\overline{(\alpha_1,\alpha_1)}&&\overline{(\alpha_1,\alpha_2)}&&\cdots&&\overline{(\alpha_1,\alpha_p)}\\\overline{(\alpha_2,\alpha_1)}&&\overline{(\alpha_2,\alpha_2)}&&\cdots&&\overline{(\alpha_2,\alpha_p)}\\\vdots&&\vdots&&\ddots&&\vdots\\\overline{(\alpha_p,\alpha_1)}&&\frac{\vdots}{(\alpha_p,\alpha_2)}&&\cdots&&\overline{(\alpha_p,\alpha_p)}\end{pmatrix} \\&==\begin{pmatrix}|\alpha_1|^2&\overline{(\alpha_1,\alpha_2)}&\cdots&\overline{(\alpha_1,\alpha_p)}\\\overline{(\alpha_2,\alpha_1)}&|\alpha_2|^2&\cdots&\overline{(\alpha_2,\alpha_p)}\\\vdots&\vdots&\ddots&\vdots\\\overline{(\alpha_p,\alpha_1)}&\overline{(\alpha_p,\alpha_2)}&\cdots&|\alpha_\text{p}|^2\end{pmatrix}\end{aligned}$
## <font color=blue>正交</font><font color=codespan>orthogonal</font>



- <font color=green>定义</font>
  - $\begin{aligned}X\bot Y\iff(X,Y)=0& =x_1\overline{y_1} +x_2\overline{y_2} +\cdots+x_n\overline{y_n} \\&=\overline{\overline{x_1}\left.y_1\right.+\overline{x_2}\left.y_2\right.+\cdots+\overline{x_n}\left.y_n\right.} \\=(Y,X)\end{aligned}$
- <font color=green>性质</font>
  - $X\perp Y\iff\big(Y,X\big)=\overline{(X,Y)}=y_1\overline{x_1}+y_2\overline{x_2}+\cdots+y_n\overline{x_n}=0.$
  - $X\perp Y\iff(Y,X)=0\iff(X,Y)=0$
  - $X\perp Y\iff\mathrm{X}^HY=0\iff Y^HX=0$
  - $X\bot Y\Rightarrow aX\bot bY$
  - $\begin{aligned}& X_1\perp X_2\perp\cdots\perp X_n\Rightarrow|c_1X_1\pm c_2X_2 \pm\cdots\pm c_nX_n|^2=|c_1X_1|^2+ |c_2X_2|^2+\cdots+|c_nX_n|^2\\\\&\text{此时，} X_1,X_2,\cdots,X_n \color{red}\text{称为一个正交组}\end{aligned}$
- <font color=green>tips</font>
  - 零向量θ与任何向量均正交
  - 正交向量组要求向量均为<u>非零向量</u>
  - 正交向量组<u>线性无关</u>
  - 向量 $X$ 与 $Y$ 正交当且仅当 <font color=red>$‖X+Y‖^2=‖X‖^2+‖Y‖^2$</font>
    勾股定理
  - 在 $n$ 维内积空间中，正交向量组中的向量个数不会超过n个
  - 拓展
    - ![](https://api2.mubu.com/v3/document_image/21954114_72b9b71b-8d0a-40b5-f894-754fbac171ba.png)
## <font color=blue>矩阵合同</font>



- 若$P^HAP=B(P可逆)$，则$A$与$B$ 合同，记为 $A\triangleq B$
- <mark>基本性质</mark>
  - <mark>对 称 性</mark> : $A\triangleq B\Longleftrightarrow B\triangleq A$
  - <mark>传 递 性</mark> : $A\triangleq B, \triangleq \Longleftrightarrow A\triangleq C$
## <font color=blue>矩阵相似</font>



- <font color=green>定义</font>
- <font color=green>tips</font>
  - 两矩阵相似的充分必要条件是两矩阵的特征矩阵等价
## <font color=blue>矩阵的秩</font>



- [H 阵的秩](https://mubu.com/app/edit/home/60ee0FTFmM0#o-7JzxsOVlA5)
- 矩阵秩越乘越小：$r(AB)<min\{r(A),r(B)\}$
## <font color=blue>零化多项式</font>



- <mark>定义</mark>
  - 给定矩阵$A∈ℂ^{n×n}$
  - 若存在多项式$g(λ)$使得$g(A)=0$
  - 则称$g(λ)$为$A$的零化多项式
- <mark>性质</mark>
  - 复方阵A的零化多项式有无数个，A阵特征多项式的所有倍式都是A阵的零化多项式
## <font color=blue>首1多项式</font>



- 对于一元多项式 <font color=red>$g(λ)=a_nλ^n+a_{n−1}λ^n−1+⋯+a_1λ+a_0$</font>
- 如果 $a_n≠0$，则称 <font color=red>$a_nλ^n$</font>为多项式的首项
- $n$ 称为 $g(λ)$ 的次数，记为 <font color=red>$deg\big(g(λ)\big)=n$</font>
- $a_n$ 称为 $g(λ)$ 的首项系数
- 若<font color=red> </font><font color=red>$a_n=1$</font>，则称 $g(λ)$ 为<mark>首1多项式</mark>
## <font color=blue>最小多项式</font>



- <mark>定义</mark>
  - 复方阵A的零化多项式中最小次数的<font color=blue>首1多项式</font>称为矩阵A的最小多项式
  - $m_A(λ)$
- <mark>性质</mark>
  - 矩阵A的最小多项式$m_A(λ)$是唯一的，且可整除矩阵A的任一零化多项式
    - 特别的 $m_A(λ) | f_A(λ)$
  - 矩阵A的特征多项式$f_A(λ)$与最小多项式$m_A(λ)$具有相同的根（不计重数）
## <font color=blue>Jordan块</font>参考



- <font color=green>定义</font>
  - <font color=red>Jordan块</font>
    - ![](https://api2.mubu.com/v3/document_image/21954114_71a38d43-d51a-43e9-b870-650953477a34.png)
  - <font color=red>Jordan标准形</font>
    - ![](https://api2.mubu.com/v3/document_image/21954114_770ec21a-bc46-4c60-aa91-daba49d16d5c.png)
    - <mark>例子</mark>
      - ![](https://api2.mubu.com/v3/document_image/21954114_e0f1b31d-fcec-46f7-bfdc-d1525a081411.png)
- <font color=green>定理</font>
  - <mark>Jordan标准形定理</mark>
    - 设矩阵J是复方阵A的Jordan标准形，则矩阵A与矩阵J相似
    - 例子
      - 题目
        - ![](https://api2.mubu.com/v3/document_image/21954114_09e2cb3a-b0ca-4eda-e41b-f3e5c96b485b.png)
      - 解答 to-do
  - <mark>Frobenious定理</mark>
    - 设 $A∈ℂ^{n×n}$
    - 其特征矩阵 $λI−A$ 的Smith标准形为 $diag(d_1(λ),…,d_n(λ))$
    - 则A的最小多项式$m_A(λ)=d_n(λ)$
- <font color=green>tips</font>
  - 任一Jordan块的最小多项式等于它的特征多项式，也是Jordan块所对应特征矩阵的初等因子
    - 给定初等因子所作的最简λ矩阵就是Jordan块的特征矩阵
  - Jordan块本身就是一个Jordan矩阵
  - 对角矩阵是一个Jordan矩阵，她的每个Jordan块都是一阶的 $\Leftrightarrow$ A 的初等因子都是一次的
  - Jordan标准型中，不同Jordan块的对角线元素可能相同，故特征值$\lambda_i$的代数重数 $\ge$ $\lambda_i$ 对应的某个Jordan块的阶数
## <font color=blue>映射、变换</font>#to-do



- 设 $V$ 和 $W$ 是两个非空集合，$f$ 是 $V$ 到 $W$ 的一个映射
- <font color=green>单射</font>
  - 对任意 $x_1,x_2∈V$， 当 $x_1≠x_2$ 时有 $f(x_1)≠f(x_2)$
- <font color=green>满射</font>
  - 对任意 $y∈W$ 都有一个元素 $x∈V$ 使得 $f(x)=y$
    即存在原像
- <font color=green>双射</font>
  - $f$ 既是单射，又是满射
    即一一对应
- 变换
  - 设 $V$ 是一个非空集合，<u>$V$</u><u> 到自身的映射</u>称为 $V$的<mark>变换</mark>
  - V到自身的<u>双射</u>称为V的<mark>一一变换</mark>
  - 若V是<u>有限集</u>，V的一一变换称为V的<mark>置换</mark>
- 线性映射、线性变换
  - 定义
    - 设 $V$ 和 $W$ 是数域 $F$ 上的线性空间，如果映射 <font color=red>$T:V→W$</font>满足下述性质
      - <mark>可加性</mark>：$∀x,y∈V，T(x+y)=T(x)+T(y)$
      - <mark>齐次性</mark>：$∀λ∈F，T(λx)=λT(x)$
    - 称 $T$ 为 $V$ 到 $W$ 的一个线性映射
    - 当 $V=W$ 时， 称 $T$ 为 $V$ 上的<u>线性变换</u>
  - 特殊的线性变换1
    定义映射 
    - <font color=red>零变换</font>：$T(x)=θ， ∀x∈V$
    - <font color=red>恒等变换</font>：$T(x)=x，∀x∈V$
    - <font color=red>负变换</font>：$T(x)=− x，∀x∈V$
  - 特殊的线性变换2
    定义 ​
    - <font color=red>伸缩</font>：$T(x)=\bigg[ \begin{matrix} k_1 & 0 \\ 0 & k_2 \end{matrix} \bigg]x$
       和 为正常数
      ​
    - <font color=red>反射</font>：$T(x)=(x_1,−x_2)$
    - <font color=red>旋转</font>：$T(x) = \bigg[ \begin{matrix} cos\varphi & -sin\varphi \\sin\varphi & cos\varphi \end{matrix}\bigg]x$
       为旋转角
  - 正交投影变换
    - 设 $W$ 是线性空间 $V$ 的<u>非平凡子空间</u>，定义 $V$ 上的<font color=red>正交投影变换</font>映射 $T$为
    - <font color=red>$T(x)=\mathrm{Proj_W}x$</font>
    - 若$\alpha_1,\cdots,\alpha_p$ 为 $W$ 的标准正交基
      - $T(x)=\mathrm{Proj_W}x\\=(x,\alpha_1)\alpha_1+(x,\alpha_2)\alpha_2+\cdots+(x,\alpha_p)\alpha_p$

# <font color=purple>重要公式、定理</font>

## <font color=blue>许尔公式</font>



- $每个n 阶方阵\mathbf{A}=\mathbf{A}_{n\times n}\\ \text{都存在优阵 }\mathbf{Q}\\ \text{ 使得}\mathbf{Q}^{-1}\mathbf{A}\mathbf{Q}=\mathbf{D}=\begin{pmatrix}\lambda_1&\cdots&*\\&\ddots&\vdots\\0&&\lambda_n\end{pmatrix}\text{为上三角}$
- 优相似三角化：每个方阵 A 优相似于上三角
- <mark>Schur引理</mark>
  - 任意复方阵A优相似于上三角阵Λ
  - 即存在U阵 $U$ 使得 $U^HAU=Λ$
    - $U^HAU=Λ$
    - $Λ$——上三角矩阵
    - $U$——U阵
- <mark>实方阵Schur引理</mark>
  - 设$A∈ℝ^{n×n}$的特征值均为实数，则存在正交矩阵 $Q$ 使得
    - ![](https://api2.mubu.com/v3/document_image/21954114_7d62bc79-7b96-4cb1-f3ec-3ee780008f1f.png)
- <mark>tips</mark>
  - Schur引理表明任意复方阵都相似于上三角阵，但并不是所有复方阵都相似于对角阵
  - 可酉相似对角化的矩阵
    - 正规阵
      - Hermite阵、反Hermite阵、正交阵、酉矩阵等都是正规阵
## <font color=blue>换位公式</font>



- - ![](https://api2.mubu.com/v3/document_image/29f02167-2ac4-488f-bc58-bf085981538f.jpeg)
- - ![](https://api2.mubu.com/v3/document_image/21954114_d1ff572c-9ade-486a-8551-8aaa1a03f551.png)
- - ![](https://api2.mubu.com/v3/document_image/21954114_e7f5d0c0-6162-4fd5-9188-f6c2aa5ceb93.png)
- - ![](https://api2.mubu.com/v3/document_image/21954114_bbb0e451-0403-49ee-a86d-885499c2a268.png)
## <font color=blue>特商公式</font>



- $\displaystyle\lambda=\frac{X^HAX}{|X|^2},\text{其中}(X\neq0\text{为}\lambda\text{的一个特征向量})$
  - $\text{证明}:X^HAX=X^H\lambda X=\lambda X^HX=\lambda|X|^2(|X|^2>0)$
## <font color=blue>平方公式</font>



- <mark>若 </mark>$A$ 为半正定（$A\ge 0$），或 $A$ 为正定（$A>0$）
- <mark>则有</mark>分解 $A=B^2$，且 $B^H=B$ 为<mark> </mark><mark>$Hermite$</mark><mark> 半正定</mark>（$B\ge0$）
- $B$ 叫 $A$ 的平方根，记作 $\displaystyle B=\sqrt{A}=A^{\frac12}$
## <font color=blue>秩公式</font>



- $r(AA^H)=r(A^HA)=r(A)$
## <font color=codespan>Cayley</font><font color=blue>定理</font>



- $n$ 阶方阵的特征多项式 $T(x)=|xI-A|$ 也是它的一个 0 化式，$\\$即有 $T(A)=0$
- 例题
  - - ![](https://api2.mubu.com/v3/document_image/21954114_6a512604-ef08-41ef-abb6-e741a72e2681.png)
## <font color=codespan>Cauchy—Schwarz</font><font color=blue>不等式</font>



- <font color=green>定义</font>
  - 设V是数域F上的内积空间，对 $\forall x, y∈V$，有 <font color=red>$|(x,y)|≤‖x‖‖y‖$</font>
  - 其中等号成立当仅当 <font color=red>$x, y$</font><font color=red>线性相关</font>
- <font color=green>拓展</font>
  定义不同内积可得到不同的Cauchy不等式
  - 对 $ℝ^n$ 中任两向量 <mark>$x=[x_1,⋯,x_n]^T$</mark>和 <mark>$y=[y_1,⋯,y_n]^T$</mark>
    - $\displaystyle \left|\sum_{i=1}^nx_iy_i\right|\leq\sqrt{\sum_{i=1}^nx_i^2}\sqrt{\sum_{i=1}^ny_i^2}$
## <font color=blue>亏加秩定理</font>



- 设 $T∈L(V,W)$
- <font color=red>$dimN(T)+dimR(T)=dimV$</font>
- 即线性映射 $T$ 的亏加秩等于其定义域 $V$ 空间的维数



