矩阵理论1

# <font color=purple>特殊矩阵</font>

---
## <font color=blue>H 阵</font>



>`Hermite matrix`

### <font color=green>定义</font>



- <font color=red>$A=A^H \in C^{n\times n}$</font>
### <font color=green>判定</font>



>A是Hermite矩阵的充要条件

- ①存在酉矩阵 $U$ 使得 <font color=red>$U^HAU=\Lambda= \mathbf{diag}(\lambda_1,\cdots,\lambda_n)$</font>
  >$\lambda_1,\cdots,\lambda_n$ 均为实数
- ②对任意方阵$S$ ，$S^HAS$ 为Hermite矩阵
- 如果 A , B 是Hermite阵，则$AB$ 是Hermite矩阵的充要条件是$AB=BA$
### <font color=green>性质</font>



- 主对角线元素`对角元`为实数
  - $A=\begin{pmatrix}a_{11}&&&*\\&a_{22}&&\\&&\ddots&\\*&&&a_{nn}\end{pmatrix}A^H=\begin{pmatrix}\overline{a_{11}}&&&*\\&\overline{a_{22}}&&\\&&\ddots&\\*&&&\overline{a_{nn}}\end{pmatrix}$
- $A$ 有 $n$ 个互相正交的特征向量，即 $X_1\bot X_2\bot...\bot X_n$
  >$A$ 的不同特征值所对应的特征向量是相互正交的
  - proof
    ![](https://api2.mubu.com/v3/document_image/21954114_47c562e0-65dd-4f49-de96-01d9083a624b.png)
- $a_{i,j}=\overline{a_{j,i}}$
  >$1\leq i,j\leq n$
- 任何<mark>实对称矩阵</mark>是`Hermite`矩阵
- 每个<font color=red>$H$</font><font color=red>阵</font>$A$ <mark>优相似于对角阵</mark>
  - 存在U阵 $Q$ 使 <font color=red>$Q^{-1}AQ=Q^HAQ=\Lambda=\begin{pmatrix}\lambda_1&&\\&\ddots&\\&&\lambda_n\end{pmatrix}\\ A=Q\Lambda Q^{-1}=Q\Lambda Q^H$</font>，且 $\lambda(A)\in R$
    - proof
      ![](https://api2.mubu.com/v3/document_image/21954114_75076d8d-7ce5-4964-bb3f-bf6dea24e641.png)
- <mark>特征根都是实数</mark>，$\{\lambda_1,\cdots,\lambda_n\}\in R$
  - proof
    ![](https://api2.mubu.com/v3/document_image/21954114_b320c4bf-9edf-44f1-c71d-6c702fb479ab.png)
- 对正整数 $k$，$A^k$ 也是 $H$ 阵
- 若 $A$ 可逆，$A^{-1}$ 也是 $H$ 阵
- 对实数 $k , p$ ，$k A + p B$ 也是Hermite矩阵
  >(A , B为n 阶Hermite矩阵)
- 任一复方阵都可以<strong>唯一</strong>地表示成Hermite矩阵和反Hermite矩阵之和
### <font color=green>乘积形式的H阵性质</font>



- 对一切矩阵$A=A_{n\times p}$ 且 $n\geq p$ ，$A^HA$与$AA^H$都是`Hermite`阵
  - proof
    ![](https://api2.mubu.com/v3/document_image/21954114_7ba61f5c-9ffc-4ab6-d3b2-c7adaff2516f.png)
- $AA^H$ 矩阵的迹
  - $A_{n\times p}=\begin{pmatrix}a_{11}&\cdots&a_{1p}\\\vdots&\ddots&\vdots\\a_{n1}&\cdots&a_{np}\end{pmatrix}\in C^{n\times p}\\ A_{p\times n}^H=\begin{pmatrix}\overline{a_{11}}&\cdots&\overline{a_{n1}}\\\vdots&\ddots&\vdots\\\overline{a_{1p}}&\cdots&\overline{a_{np}}\end{pmatrix}\in C^{p\times n}$
  - <font color=red>$\displaystyle tr(A^HA)=tr(AA^H)=\sum\limits_{i=1,j=1}^n{|a_{ij}|^2}$</font>
  - <strong>推论</strong>
    - $tr(AB^H)=tr(B^HA)=\sum a_{ij}\overline{b_{ij}}$
- $A^HA$ 与 $AA^H$只相差 $n-p$ 个 0 根
  - proof
    ![](https://api2.mubu.com/v3/document_image/21954114_456a6946-33e1-4c54-8b93-5635b7dc5b50.png)
- $A^HA$ 与 $AA^H$ 是<strong>半正定阵</strong>
  - proof
    ![](https://api2.mubu.com/v3/document_image/21954114_6c98f7d6-2751-4613-ee5f-1247e7978663.png)
- $r(AA^H)=r(A^HA)=r(A)=r(A^H)$
  - proof 1
    ![](https://api2.mubu.com/v3/document_image/21954114_625102e6-be5d-4ae6-b7cf-4d8668b4e94d.png)
  - proof 2——只需证$A^HAX= 0$ 的解也是 $AX=0$ 的解
    ![](https://api2.mubu.com/v3/document_image/21954114_f0969394-dba4-4830-a01a-61a838edf46d.png)
---
## <font color=blue>二次型、正定阵</font>



>`参考来源` [csdn](https://blog.csdn.net/hzf0701/article/details/134824086)

### `Hermite`<font color=green>二次型定义</font>



- 令 $A^H=A\in \Bbb C^{n\times n}$，$X=\begin{pmatrix}x_1\\x_2\\\vdots\\v_n \end{pmatrix}$
- 称 $X^HAX=(\overline{x_1},\overline{x_2},\cdots,\overline{x_n}) A\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix}\\$为矩阵 $A$ 产生的二次型，记作 $f(x)=X^HAX$
### <font color=green>正定二次型与正定阵定义</font>



- 若$A^H=A$ ，对一切$X\neq0$ ，有$X^HAX>0$ ，则$f(x)=X^HAX$为<mark>正定二次型</mark>，$A$为<mark>正定阵</mark>，记为 $A>0$
- 若$A^H=A$ ，对一切$X\neq0$ ，有$X^HAX\geq0$ ，则$f(x)=X^HAX$为<mark>半正定二次型</mark>，A为<mark>半正定阵</mark>，记为 $A\geq0$
- <strong>补充定义</strong>
  ![](https://api2.mubu.com/v3/document_image/21954114_ed06eb89-6c17-4b0b-9559-3fcfdea2cdf1.png)
### <font color=green>判定</font><font color=green>$n$</font><font color=green>阶Hermite矩阵</font><font color=green>$A$</font><font color=green>正定</font>



- all
  ![](https://api2.mubu.com/v3/document_image/21954114_9ac3669d-614f-407d-f362-05549e35cb18.png)
### <font color=green>正定阵定理</font>



- <font color=red>$A>0\Longleftrightarrow A$</font><font color=red>为Hermite阵，且</font><font color=red>$\lambda_1,\lambda_2,\cdots,\lambda_n>0$</font>
  - proof
    ![](https://api2.mubu.com/v3/document_image/21954114_e18ba551-1d01-4828-9864-b892facf5c7c.png)
- <font color=red> </font><font color=red>$A\geq0\iff A$</font><font color=red>为Hermite阵，且</font><font color=red>$\lambda_1,\lambda_2,\cdots,\lambda_n\geq0$</font>
- <mark>单位阵是正定阵</mark>
- <mark>正定阵间必合同</mark>
  - $A >0 \iff A \triangleq \Lambda$
  - $\Lambda \triangleq I$
  - 若 $A,B$ 为同阶正定阵，则 $A \triangleq B$
  - proof
    ![](https://api2.mubu.com/v3/document_image/21954114_dff8a744-3754-48b0-dc7d-d5fc47a3d3f0.png)
### <strong>补充</strong>



- 实正定阵的重要结论
  ![](https://api2.mubu.com/v3/document_image/21954114_51def1d6-93b6-474f-a962-27c58d20e1a5.png)
---
## <font color=blue>斜H阵</font>



>`Skew-Hermit`

- $A^H=-A$
- <mark>性质</mark>
  - 对角元为纯虚数
  - 若 $B$ 是 `skew-Hermit` $\rightarrow$ $iB$ 与 $\displaystyle \frac{B}{i}$ 都是`Hermit`
  - 若 $A$ 是 `Hermit` $\rightarrow$ $iA$ 与 $\displaystyle \frac{A}{i}$ 都是`Skew-Hermit`
  - $A$ 是 `Hermit` $\Leftrightarrow$ $iA$ 是 `Skew-Hermit`
---
## <font color=blue>正交阵</font>



- <font color=red>$A^TA=AA^T=I$</font>
- <mark>性质</mark>
  - 正交矩阵的任一行（列）同时乘以−1时，得到的新矩阵仍为正交矩阵
  - 正交阵的所有特征值的模值为1
  - 正交阵的行列式必为 $\pm1$
  - 正交阵的乘积仍为正交阵
- <mark>判定</mark>
  - <strong>定义法</strong> $A^TA=AA^T=I$
  - $n$阶实方阵$A$是正交矩阵<u>当且仅当</u>
    - $A$的<strong>所有特征值的模值为</strong><strong>$1$</strong>
    - 且存在酉矩阵$U$使得 <font color=red>$U^HAU=diag(λ_1,⋯,λ_n)$</font>
      >其中$λ_1,⋯,λ_n$是A的n个特征值
---
## <font color=blue>优阵（U阵）</font>



- 如果 $A=(\alpha_1,\alpha_2,\cdots,\alpha_n)_{n\times n}$ 是<font color=green>预优阵</font>且$|\alpha_1|=|\alpha_2|=\cdots=|\alpha_p|=1$，那么$A$ 是一个优阵
- <mark>判定</mark>
  - $A=(\alpha_1,\alpha_2,\cdots,\alpha_n)_{n\times n}$是U阵 $\iff$
    - <font color=red>$|\alpha_1|=|\alpha_2|=\cdots=|\alpha_p|=1$</font>
    - 且 <font color=red>$\alpha_1\perp\alpha_2\perp\cdots\perp\alpha_n$</font>
  - <font color=red>$A=A^{n\times n} 是 U阵 \\ \Leftrightarrow A^{H} A=I_{\mathrm{n}} \\ \Leftrightarrow A^{-1}=A^{H} \\ \Leftrightarrow AA^{H}=I_{\mathrm{n}}$</font>
    >$\because AA^{-1}=I$
    - 注意：U阵必可逆
  - $n$阶复方阵$A$是U阵<u>当且仅当</u>
    - $A$的<strong>所有特征值的模值为</strong><strong>$1$</strong>
    - 且存在酉矩阵$U$使得 <font color=red>$U^HAU=diag(λ_1,⋯,λ_n)$</font>
      >其中$λ_1,⋯,λ_n$是A的n个特征值
- <mark>性质</mark>
  >如果 A 是U阵
  - 如果 $A_{n,n}和B_{n,n}$ 是U阵 $\Rightarrow$ $AB$是U阵
  - $A 是U，且X_1\bot X_2\cdots\bot X_p \Rightarrow$ $AX_1\bot AX_2\cdots\bot AX_p$
  - $k=\pm1,kA=(k\alpha_1,k\alpha_2,\cdots,k\alpha_n)\text{ 为优阵}$
  - $B=(\beta_1,\beta_2,\cdots,\beta_n)$为优阵，其中$\beta\text{ 组为 }\alpha\text{ 组的重排}$
  - $|Ax|^2=|x|^2$
    ![](https://api2.mubu.com/v3/document_image/ab81598e-2cf4-420a-be0e-01a78666e299-21954114.jpg)
  - $x\bot y\Rightarrow Ax\bot Ay$
    ![](https://api2.mubu.com/v3/document_image/c235ea90-ad61-4a9c-98c1-0b60ca48e31e-21954114.jpg)
  - $(Ax,Ay)=(x,y)$
- <mark>拓展性质</mark>
  - U阵的任一行（列）同时乘以模为1的任何数后，得到的新矩阵仍为U阵
  - U阵的乘积仍为U阵
  - $A$ 所有特征值的模值为1，行列式的模值为1
---
## <font color=blue>正规阵</font>



- 方阵 $A$ 满足 $A^HA=AA^H$
  >正规阵必为方阵
- <font color=green>判定</font>
  - <font color=blue>H 阵 </font>、<font color=blue>斜H阵</font>、<font color=blue>正交阵</font>、（包含实正交阵）都是正规阵
  - <strong>对角阵</strong>一定是正规阵
  - 严格三角阵（非对角形）一定不是正规阵
  - <strong>实对称</strong>与<strong>实反对称阵</strong>都正规
  - 复方阵 $A$ 是正规矩阵 <mark>当且仅当</mark> $A$ 有 $n$ 个<strong>特征向量</strong>构成$\Bbb C^n$ 空间的<strong>一组标准正交基</strong>，且属于 $A$的<strong>不同特征值的特征向量</strong><strong><u>正交</u></strong>
  - 复方阵 $A$ 是正规矩阵 <mark>当且仅当</mark> $A$ <u><font color=underline>酉相似于对角阵</font></u>
  - $n$阶方阵$A$正规的<u>充分必要条件</u>是它与一个具有互异的特征值且与$A$有相同的特征向量的矩阵$B$可交换(即$AB=BA$)
  - 若两个正规矩阵可交换，则它们的乘积也是正规矩阵
    - proof
      ![](https://api2.mubu.com/v3/document_image/21954114_06e0762d-346f-464d-dccc-304938a03129.png)
- <font color=green>性质</font>
  - 若$A$正规，则$kA＋cI$正规
  - 若$A$正规，则$A$与$A^H$必有相同特征向量
    - 即若$A$正规，且$AX＝cX$，则$A^HX＝\bar{c}X$
  - 若$A$正规，则$Q^HAQ$也正规，其中$Q$为U阵（$QQ^H＝I$）
    >正规阵的优相似必正规
  - 若$A$正规，则任意多项式$f(A)＝λ_ 0 I+λ _1 A+λ _2 A ^2 +⋯+λ_nA^K$也正规
    >多项正规定理——正规阵的多项式也正规
  - 正规阵的奇异值为特征值的绝对值
- <font color=green>易错</font>
  - × 若A是正规矩阵，则A的特征向量必两两正交
- <font color=green>引理</font>
  - $\text{若分块阵 }A=\begin{pmatrix}B&C\\0&D\end{pmatrix}\text{正规，则 }C=0\text{，且 }B,D\text{ 都正规，即 }A=\begin{pmatrix}B&0\\0&D\end{pmatrix}$
---
## <font color=blue>度量矩阵</font>



>`Gram Martrix`

- <font color=green>定义</font>
  - 设$ϵ_1,⋯,ϵ_n$是内积空间 $V$ 中的一组基，称n阶矩阵A 为$V$ 关于基 $ϵ_1,⋯,ϵ_n$ 的度量矩阵
    ![](https://api2.mubu.com/v3/document_image/21954114_376d9da9-7e0c-4514-dda6-8c28ae613170.png)
  - 记为 <font color=red>$G(ϵ_1,⋯,ϵ_n)$</font>
- <font color=green>tips</font>
  - 内积空间中内积与度量矩阵是一一对应的
  - <font color=red>$(x,y)=η^HA^Hξ$</font>
    - 设 $ϵ_1,⋯,ϵ_n$ 是内积空间V的一组基，则 $∀x,y∈V$,有
      ![](https://api2.mubu.com/v3/document_image/21954114_d1334d12-5a51-43f6-9053-0b6c515803cf.png)
- <font color=green>性质</font>
  >设 $G(ε_1,⋯,ε_n)$ 和$G(ϵ_1,⋯,ϵ_n)$ 均为内积空间 $V$ 的度量矩阵
  - $G(ε_1,⋯,ε_n)$ 和 $G(ϵ_1,⋯,ϵ_n)$ 是<strong>正定Hermite矩阵</strong>
  - $G(ε_1,⋯,ε_n)$ 和 $G(ϵ_1,⋯,ϵ_n)$ <strong>合同</strong>
    - 即存在非奇异矩阵（可逆矩阵） $P$ 使得
    - $P^HG(ε_1,⋯,ε_n)P=G(ϵ_1,⋯,ϵ_n)$
    - $P$ 是由基 $ε_1,⋯,ε_n$ 到基$ϵ_1,⋯,ϵ_n$ 的过渡矩阵
---
## <font color=blue>Householder矩阵</font>



- <font color=green>定义</font>
  - 设 $w∈ℂ^n$ 是<strong>单位向量</strong>
  - $H(w)=I−2ww^H$
- <font color=green>性质</font>
  - $\big(H(w)\big)^H=H(w)=\big(H(w)\big)^{−1}$
  - $|H(w)|=−1$
    >特征值 n-1个1， 1个 -1
  - 设 $x, y∈ℂ^n$ 且$x≠y$，则存在单位向量 $w$ 使得$H(w)x=y$ 的<strong>充分必要条件</strong>是
    - $x^Hx=y^Hy\quad,x^Hy=y^Hx$
    - 此时可取 $\displaystyle w=\frac{e^{iθ}(x−y)}{‖x−y‖}$
      >其中θ为任一实数，实际求就取0
  - 一定可以酉相似对角化
---
## <font color=blue>奇异矩阵</font>



- $|A|=0$
- 没有逆矩阵
---
## <font color=blue>λ矩阵</font>



### <font color=green>定义</font>



- 以 <strong>λ多项式</strong> 为元素的矩阵称为$\lambda$矩阵，记为`A(λ)`
  - <mark>$A(λ)=[a_{ij}(λ)]_{m×n}$</mark>
    >$a_{ij}(λ)∈P_n(λ)$
### <strong><font color=bold>λ矩阵的秩</font></strong>



- 矩阵$A(λ)$中<strong><u>非零子式的最高阶数r</u></strong> 定义为$A(λ)$的秩，记为`rank(A(λ))=r`
- 例子
  ![](https://api2.mubu.com/v3/document_image/21954114_81336d7f-e5a5-482e-b7fb-c838996a23b9.png)
### <strong><font color=bold>λ矩阵相抵</font></strong>



- <mark>定义</mark>
  - 若$\lambda$矩阵$A(\lambda)$经过<mark>有限次初等变换</mark>化为$B(\lambda)$，则称$A(\lambda)$与$B(\lambda)$<font color=red>相抵</font>
    - <strong>$\lambda$</strong><strong>矩阵的初等变换</strong>
      ![](https://api2.mubu.com/v3/document_image/21954114_cf60ebf5-9784-4ff5-abb0-cfbf452f57e5.png)
  - 即存在<strong>可逆阵</strong> $P(\lambda)$ 和 $Q(\lambda)$，使得 <font color=red>$A(\lambda ) = P(\lambda)B(\lambda)Q(\lambda)$</font>
  - $A(λ)≅B(λ)$
- <mark>判定</mark>
  - $\lambda$矩阵$A(\lambda)$与$B(\lambda)$相抵 的<mark>充要条件</mark>
    - <font color=red>or</font> 完全一致的<font color=green>不变因子</font>
      - 即Smith标准型相同
    - <font color=red>or </font>具有相同的<font color=green>各阶行列式因子</font>
      - <strong>行列式因子</strong>
        >注意：行列式因子的个数=$\lambda$矩阵的秩！
        - 设 $\lambda$ 矩阵 $A(\lambda)$ 的秩为 $r$，对于正整数<font color=red> </font><font color=red>$1\le k\le r$</font>，$A(\lambda)$ 的全部 $k$ 阶子式的<strong>首1最大公因式</strong>称为 $k$ 阶行列式因子，记作$D_k(\lambda)$
        - 例子
          ![](https://api2.mubu.com/v3/document_image/21954114_c01ee1be-7a00-4d02-d39f-9a8d01e26758.png)
    - <font color=red>or</font> 完全一致的<font color=green>初等因子</font>，且 <font color=green>$rank\big (A(λ)\big)=rank\big(B(λ)\big)$</font>
- <mark>性质</mark>
  - $\lambda$矩阵<strong>相抵</strong>则其<strong>秩相同</strong>，反之则不然
  - 相抵的$\lambda$矩阵具有<strong>相同的秩</strong>和<strong>相同的各阶行列式因子</strong>
  - 复方阵A和B<strong>相似</strong>当且仅当它们的<strong>特征矩阵相抵</strong>
    - 相似与相抵之间的关系
      ![](https://api2.mubu.com/v3/document_image/21954114_f94dc556-0da1-4575-f465-23e777e6293a.png)
- 例子
  - ![](https://api2.mubu.com/v3/document_image/21954114_1db6b363-f7bb-4321-9865-fab2771358fd.png)
### <strong><font color=bold>λ矩阵的逆矩阵</font></strong>



- <mark>定义</mark>
  - 设 $A(λ)$ 是 $n$ 阶 $λ$ 方阵，若存在 $n$ 阶$λ$方阵$B(λ)$满足<font color=red>$A(λ)B(λ)=B(λ)A(λ)=I$</font> 则称λ矩阵A(λ)是可逆的，并称B(λ)为A(λ)的逆矩阵，记作<font color=red>$A(λ)^{−1}$</font>
- <mark>判定</mark>
  - <font color=red>$\lambda$</font><font color=red>方阵</font><font color=red>$A(\lambda)$</font><strong><font color=bold>可逆</font></strong><font color=red>的</font><u><font color=underline>充分必要条件</font></u><font color=red>是其</font><strong><font color=bold>行列式</font></strong><strong><font color=bold>$|A(λ)|$</font></strong><strong><font color=bold>为非零常数</font></strong>
    ![](https://api2.mubu.com/v3/document_image/21954114_69ad8dda-9bc4-4c2c-f117-29e71fc5ea01.png)
### <strong><font color=bold>Smith标准形</font></strong>



- <mark>定义</mark>
  - 设 $λ$ 矩阵 $A(\lambda)$ 的秩为 $r$
  - 此标准形为$A(\lambda)$的Smith标准形
    ![](https://api2.mubu.com/v3/document_image/21954114_7fd792fb-19e3-434c-b461-ae9f0d62d23c.png)
  - $d_i(λ)$ 是<font color=blue>首1多项式</font>，且 $d_i(λ)|d_{i+1}(λ)$
- <mark>tips</mark>
  - $A(\lambda)$不一定是方阵，故Smith标准形<u>不一定是对角阵</u>
  - Smith标准形中<font color=green>不变因子</font>与<strong>行列式因子</strong>之间的关系
    - 重要
      ![](https://api2.mubu.com/v3/document_image/21954114_a79db914-b684-4b47-9e3d-cfb939b426b8.png)
  - $\lambda$矩阵的Smith标准形是<strong>唯一</strong>的
- `<font color=codespan>Frobenious</font>`<mark>定理</mark>
  - 设 $A∈ℂ^{n×n}$
  - 其特征矩阵 $λI−A$ 的Smith标准形为 <font color=red>$\rm diag(d_1(λ),…,d_n(λ))$</font>
  - 则 $A$ 的<strong>最小多项式</strong><font color=red>$m_A(λ)=d_n(λ)$</font>
  - <mark>注</mark>：$\lambda I−A$的<strong>初等因子的最小公倍式</strong>即为矩阵$A$的最小多项式$m_A(\lambda)$
- <font color=tag>例子</font>
  - 求Smith标准型
    ![](https://api2.mubu.com/v3/document_image/21954114_fb2526dc-56ff-4daf-fe73-d4cbb3db366f.png)
    ![](https://api2.mubu.com/v3/document_image/21954114_42b71ee8-c987-4445-e010-e939aab1110a.png)
  - 求初等因子、不变因子、Smith标准型
    ![](https://api2.mubu.com/v3/document_image/21954114_15f27894-ade4-40b6-b118-22a08d706658.png)
### <font color=green>不变因子</font>



- <mark>定义</mark>
  - 在$\lambda$ 矩阵$A(\lambda)$的Smith标准形中
  - <font color=red>$d_1(λ),⋯,d_{r}(λ)$</font> 由 $A(\lambda)$唯一确定的，称为$A(\lambda)$的<strong>不变因子</strong>
- <mark>tips</mark>
  - 初等变换不改变$\lambda$矩阵的不变因子
- 例子
  - ![](https://api2.mubu.com/v3/document_image/21954114_cafc377d-3359-4655-f4ca-80031e3f788e.png)
  - ![](https://api2.mubu.com/v3/document_image/21954114_462f8b1b-36c1-4b36-ded3-e9369e0f2638.png)
### <font color=green>初等因子</font>



- <mark>定义</mark>
  - ![](https://api2.mubu.com/v3/document_image/21954114_255f8f31-cd66-4870-8690-8829c28d6b09.png)
- <font color=tag>例子</font>
  - <strong>注：初等因子组可能存在相同的因子</strong>
    ![](https://api2.mubu.com/v3/document_image/21954114_f715be59-c764-44e1-d06c-48004175799b.png)
- <mark>tips</mark>
  - 初等变换不改变$A(\lambda)$的初等因子
  - 设$\lambda$矩阵$A(\lambda)$为对角块矩阵
    >即$A(λ)=diag(A_1(λ),⋯,A_s(λ))$
    - 则 $A_1(λ),⋯,A_s(λ)$ 初等因子的全体就是$A(λ)$ 的全部初等因子
  - <font color=red>行列式</font><font color=red>$|\lambda I-A|$</font><font color=red> 等于全体初等因子的乘积</font>
### <font color=green>tips</font>



- 数字矩阵是特殊的$\lambda$矩阵
- 复方阵A的<strong>特征矩阵</strong> <font color=red>$λI−A$</font> 是$\lambda$矩阵
  - <font color=red>$λI−A$</font><font color=red> 总是满秩的</font>
  - <font color=red>行列式</font><font color=red>$|\lambda I-A|$</font><font color=red> 等于全体初等因子的乘积</font>
  - <font color=red>行列式</font><font color=red>$|\lambda I-A|$</font><font color=red> 等于n阶行列式因子</font>
- λ方阵$A(λ)$<strong>可逆</strong>的<u>充分必要条件</u>是其<strong>行列式</strong><strong>$|A(λ)|$</strong><strong>为非零常数</strong>
  - ![](https://api2.mubu.com/v3/document_image/21954114_9995b351-7c07-4d7f-85ff-7e77272a483a.png)
- 在求λ矩阵的Smith标准形、不变因子或初等因子时
  - 可先将λ矩阵作初等变换，使得变换后的矩阵为对角（块）矩阵
  - 利用[定理](https://mubu.com/app/edit/home/60ee0FTFmM0#o-JiIQAHMFiQ)求出λ矩阵的初等因子，进而求出Smith标准形和不变因子
---
## <font color=blue>单纯阵</font>



- <mark>定义</mark>
  - 1
    ![](https://api2.mubu.com/v3/document_image/21954114_2da9613c-5d80-49db-8100-7c929aee6e7f.png)
  - 2
    ![](https://api2.mubu.com/v3/document_image/21954114_58dbab2b-4db5-43b3-cc32-4eb97fa32c61.png)
- <mark>性质</mark>
  - 方阵A是单纯矩阵的<strong>充分必要条件</strong>
    - <font color=red>or</font> $A$的特征矩阵 $λI−A$的<font color=green>初等因子</font>是<strong>一次</strong>的
    - <font color=red>or</font> $A$的特征矩阵 $λI−A$ 的<font color=green>不变因子</font><strong>无重根</strong>
  - <strong>充分条件</strong>
    - 若复方阵A的<font color=blue>零化多项式</font> $g(λ)$ <u>无重根</u>，$\Rightarrow$则矩阵A是单纯矩阵
    - 若复方阵是<font color=green>幂等阵</font>，则一定可以对角化
      - ![](https://api2.mubu.com/v3/document_image/21954114_fa163e0c-e526-4819-9319-0b810a355e4e.png)
---
## <font color=blue>幂零阵、幂等阵</font>



### <font color=green>幂零阵</font>



- <mark>定义</mark>
  - <font color=red>$A^k=0$</font>，$A \in \Bbb C^{n\times n}$
- <mark>性质</mark>
  - A的全体特征根为0
  - $|A+I| =1$
    - proof
      ![](https://api2.mubu.com/v3/document_image/21954114_b18c5af5-1df6-49be-da84-e70afbddaf51.png)
### <font color=green>幂等阵</font>



>也称 $A$ 为 投影矩阵

- <mark>定义</mark>
  - $A∈ℂ^{n×n}$
  - <font color=red>$A^2=A$</font>
- <mark>性质</mark>
  >$A\in \Bbb C^{n\times n}_r$ 为幂等阵
  - <font color=red>$A^H$</font>，<font color=red>$A^∗$</font> 和 <font color=red>$I−A$</font>都是幂等矩阵
  - A 为<strong>单纯阵</strong>且<strong>相似于对角阵</strong>$\Lambda = \begin{bmatrix} I_r & 0 \\ 0 & 0 \end{bmatrix}$
  - $\rm tr(A)=rank(A)$
    - 幂等阵的特征值只能是或者0或1，$r$个1，$n-r$个0
    - proof
      ![](https://api2.mubu.com/v3/document_image/21954114_7bb21389-c221-43ea-f133-d6ce87749424.png)
  - $N(A)=R(I-A)$
    >充要条件
    - ![](https://api2.mubu.com/v3/document_image/21954114_645ff638-5e3e-4704-9572-df221506f2d8.png)
  - $\mathbb C^n=N(A) \dot{+}R(A)$
  - $\mathbb C^n=N(A) \dot{+} N(A-I)$
  - $Ax=x$ $\iff$ $x∈R(A)$
    >其中 $x\in \Bbb C^n$
    - proof
      ![](https://api2.mubu.com/v3/document_image/21954114_c22f2169-5444-4427-c1de-47e7d82b9435.png)
  - $\displaystyle \rm e^{tA}=I+(e^t-1)A$
- <mark>做题技巧</mark>
  - 若$A，B，A-B$均为投影矩阵，则$AB=BA=B$
    - proof 由$A^2=A，B^2=B，(A-B)^2=A-B\\ \Rightarrow 2B =AB+BA\\ \Rightarrow2AB=AB+ABA，2BA=ABA+BA\\ \Rightarrow AB=BA=B$
---
## <font color=blue>秩一矩阵</font>



- $A=\alpha \beta^T$，$\rm rank(A)=1$
- <font color=green>性质</font>
  >设$A$ 为 $n$ 阶 秩一矩阵
  - $A$ 的 $n$ 个特征值是 1，1 个特征值为$\rm tr(A)$
  - $\rm tr(A) = \beta^T\alpha$
  - $\rm tr(A) \neq0$ 时， $A$ 可以相似对角化
  - $\rm A^k = tr(A)^{k-1} A$
  - $\alpha$ 是 $A$ 的 $\rm tr(A)$ 特征值对应的的特征向量
  - $|\lambda I-A| = \lambda^{n-1}[\lambda-tr(A)]$
  - $m_{\lambda}(A) = \lambda [\lambda-tr(A)]$
  - $A$ 的非零奇异值为 $\|\alpha\|_2 \|\beta\|_2$
  - $\|A\|_2 = \|\alpha\|_2 \|\beta\|_2$
    >矩阵的2范数即为最大奇异值
  - $\|A\|_F = \|\alpha\|_2 \|\beta\|_2$
  - 若$B$是秩为$m$的单纯矩阵，则$B$必可写成$m$个秩一矩阵之和

# <font color=purple>重要概念</font>

---
## <font color=blue>共轭</font>`<font color=codespan>Conjugate</font>`



- 对<mark>复数</mark> $w=a+ib$
  - $\overline{w}=\overline{a+bi}=a-bi$
- <mark>矩阵的共轭</mark>——矩阵内每个元素取共轭
  - $\overline{A}=(\overline{a_{i,j}})$
- <strong><font color=bold>性质</font></strong>
  - <mark>实矩阵</mark>
    - $\overline{A}=(\overline{a_{i,j}})=(a_{i,j})=A$
  - $\text{对于任意 } A=A_{m\times n}\in\mathbb{C}^{m,n}, B=B_{m\times p}\in\mathbb{C}^{n,p}$
    - $\overline{(AB)}=(\overline{A})(\overline{B})\quad$
---
## <font color=blue>共轭转置=转置共轭</font>



- $A^H=\overline{A}^T=\overline{A^T}$
- <mark>性质</mark>
  - ${(A^H)}^H=A$
  - $(A+B)^H=A^H+B^H$
  - $(kA)^H=\overline{k}(A^H)$
    >$k\in C$ （复数）
  - $(ABC)^H=C^HB^HA^H$
  - $\displaystyle (e^A)^H=e^{A^H}$
---
## <font color=blue>矩阵的模/范数</font>



- $||A||=\sqrt{\sum|a_{i,j}|^{2}}$
---
## <font color=blue>向量的模</font>



- $|| X||=\sqrt{(X,X)}=\sqrt{\left|x_1\right|^2+\left|x_2\right|^2+\cdots+\left|x_n\right|^2}\geq0$
- <font color=green>性质</font>
  >$∀x,y∈V$ 和 $k∈F$
  - ![](https://api2.mubu.com/v3/document_image/21954114_87832f43-354c-4aef-d98c-472cddd2fdf0.png)
    ![](https://api2.mubu.com/v3/document_image/21954114_5d8b4113-7b63-4f91-8308-063542f33ccf.png)
---
## <font color=blue>迹</font>



>[参考来源](https://www.cnblogs.com/Lxk0825/p/13987066.html)

- $tr(A)=a_{11}+\ldots+a_{nn}$
- <mark>tips</mark>
  - $\rm tr(ABC)=tr(BCA)=tr(CAB)$
    - proof
      ![](https://api2.mubu.com/v3/document_image/21954114_60e035d7-ac91-4833-c101-bf4987cd5a18.png)
  - $\rm tr(kA)=k\cdot tr(A)$
  - $\rm tr(A+B)=tr(A)+tr(B)$
  - $\displaystyle \frac {\partial tr(AB)}{\partial A}=\frac {\partial tr(BA)}{\partial A}=B^T$
    >矩阵乘积的迹关于第一个矩阵的梯度等于第二个矩阵的转置
    - proof
      ![](https://api2.mubu.com/v3/document_image/21954114_02f8cb8d-dfa1-4765-edda-6a74e4965e86.png)
  - $\displaystyle \frac {\partial tr(A^TB)}{\partial A}=\frac {\partial tr(BA^T)}{\partial A}=B$
  - $\rm tr(A) =\sum_i\lambda_i$
    >矩阵的迹为所有特征值之和
  - $\rm tr(A)=tr(A^T)$
### <mark>模平方公式</mark>



- $tr(A^{H}A)=tr(AA^H)=\sum|a_{i,j}|^{2}={||A||}_F^2$
  - $\begin{aligned}tr(AA^{H})&=tr[(A^{H})^{H}A^{H}]\\&=||A^{H}||^{2}\\&=\sum|\overline{a_{ij}}|^{2}\\&=||A||_F^{2}\end{aligned}$
- 推导前提——<mark>列向量的模平方公式</mark>
  - 对于一个列向量$X$—— $X^HX={\|X\|}^2$
  - $\mathrm{tr}(X^HX)=\mathrm{tr}(XX^H)=\left|x_1\right|^2+\left|x_2\right|^2+\cdots+\left|x_n\right|^2=\sum\left|x_j\right|^2\overset{\text{记为}}{\operatorname*{=}}|\mathbf{X}|^2$
- <font color=red>推广公式</font>
  - 已知 $A=(a_{ij})_{m\times n}、B=(b_{ij})_{m\times n} \in \Bbb C^{m\times n}$ 则
    - $tr(AB^H)=tr(B^HA)=\sum a_{ij}\overline{b_{ij}}$
    - $tr(AB^T)=tr(B^TA)=\sum a_{i,j}b_{i,j}$
    - $\mathrm{tr}(XY^{H})=\mathrm{tr}(Y^{H}X)=Y^{H}X=x_{1}\overline{y}_{1}+\cdots+x_{n}\overline{y}_{n}$
      >$\mathrm{~for~}X,Y\in\mathbb{C}^{\mathrm{n}}$
      - ![](https://api2.mubu.com/v3/document_image/6cdb49a6-ac88-4312-9e5e-8107fbe14821-21954114.jpg)
      - ![](https://api2.mubu.com/v3/document_image/ab05e461-6d2a-4a0e-84c4-f35e5a0c8cbc-21954114.jpg)
---
## <font color=blue>全体特征根</font>



- $\lambda(A)=\{\lambda_1,\ldots,\lambda_n\}$
---
## <font color=blue>特征值</font>



- 设矩阵<font color=red>$A∈ℂ^{n×n}$</font>的 $n$ 个特征值为 <font color=red>$λ_1,⋯,λ_n$</font>
  - 则矩阵<font color=red>$A^m$</font> 的n个特征值为 <font color=red>$λ_1^m,⋯,λ_n^m$</font>
- 设矩阵<mark>$A∈ℂ^{n×n}$</mark>的 n 个特征值为<mark>$λ_1,⋯,λ_n$</mark>，<mark>$φ(λ)$</mark>为任一多项式
  - 则矩阵多项式<mark>$φ(A)$</mark>的n个特征值为<mark>$φ(λ_1),⋯,φ(λ_n)$</mark>
- [矩阵分析：特征值，相似度对角化，Jordan标准形_jordan标准型和特征值的关系-CSDN博客](https://blog.csdn.net/qq_42192693/article/details/122248940)
- <strong>补充性质</strong>
  - ![](https://api2.mubu.com/v3/document_image/21954114_f16570a3-28c9-40a2-e7e3-984f38e875fd.png)
### <font color=green>特征子空间</font>



- 设$\lambda$是矩阵$A\in \Bbb C^{n\times n}$的一个特征值
- <font color=red>$E(\lambda )=\{x∈\Bbb C^n|Ax=\lambda x\}$</font>
- $E(\lambda )$是$\Bbb C^n$的<strong>线性子空间</strong>，称为<strong>属于特征值</strong><strong>$\lambda$</strong>的<mark>特征子空间</mark>
- <font color=red>$\rm dim E(λ_i)=n−rank(\lambda_i I−A)$</font>为特征值$\lambda_i$的<mark>几何重数</mark>
  - <mark>代数重数</mark>
  - 矩阵$A$的特征值$λ_i$作为特征方程根的重数，称为特征值$\lambda_i$的<strong>代数重数</strong>
  - `!!!` 几何重数$\leq$代数重数
    - 复方阵某一特征值的代数重数为1，则它的几何重数必为1
    - 示例
      ![](https://api2.mubu.com/v3/document_image/21954114_6a0c897e-c82b-412b-a7b4-3abb0e67f9b2.png)
- $\rm dim(E(\lambda))\ge1$
---
## <font color=blue>右逆、左逆</font>



- A有<strong>右逆</strong> 的充要条件（即存在矩阵B使得$AB= I$）
  - A为<strong>行满秩</strong>矩阵
- A有<strong>左逆</strong> 的充要条件（即存在矩阵B使得$BA= I$）
  - A为<strong>列满秩</strong>矩阵
---
## <font color=blue>内积</font>`<font color=codespan>Inner product</font>`



### <font color=green>定义在</font><font color=green>$\Bbb C^n$</font><font color=green>（列） 上的内积</font>



>$X$与$Y$ 都是 $C^n$ 上的列向量

- <mark>$X$</mark><mark>与</mark><mark>$Y$</mark><mark>的标准内积</mark>
  - $(X,Y)=Y^HX=\mathrm{tr}(XY^H)=x_1 \overline{y_1}+\cdots+x_n \overline{y_n}$
    >$X=\begin{pmatrix}x_{1}\\\vdots\\x_{n}\end{pmatrix}, Y=\begin{pmatrix}y_{1}\\\vdots\\y_{n}\end{pmatrix}\in\mathbf{C}^{n}$
  - $YX^H=(Y,X)=\overline{(X,Y)}$
- <mark>特例</mark>
  - $(X,X)=\mathrm{tr}(XX^H)=X^HX=x_1\overline{x_1}+\cdots+x_n\overline{x_n}=\mid x_1\mid^2+\cdots+\mid x_n\mid^2=\mid X\mid^2$
- <mark>特性</mark>
  - $\mid X\mid^2=(X,X)=\mathrm{tr}(XX^H)=\mathrm{tr}(X^HX)=X^HX=\mid X\mid^2$
  - $Y^HX=(X,Y) \\$ $X^HY=(Y,X)=\overline{(X,Y)}$
  - $\mid kX\mid=\mid k\parallel X\mid\\ \mid\frac{X}{k}\mid=\frac{\mid X\mid}{\mid k\mid},(k\neq0);\quad\\ \mid X\pm Y\mid\leq\mid X\mid+\mid Y\mid.$
    >模长性质
  - 如果 $X \ne 0$ 则 $\frac{X}{|X|}$ 是单位向量
    >单位化公式
- <mark>内积性质</mark>
  - $(X,X)\ge 0$
  - $(Y,X)=\overline{(X,Y)}$
  - $(kX,Y)=k(X,Y)\\ (X,kY)=\overline{k}(X,Y)$
    >$k\in C$
  - $(X+Y,W)=(X,W)+(Y,W),\\(W,X+Y)=(W,X)+(W,Y)$
  - $| (X,Y) |^{2}\leq(X,X)(Y,Y)\\ \mathrm{i.e.} | (X,Y) |\leq| X |\cdot| Y|$
### <font color=green>定义在</font><font color=green>$\Bbb C^{m\times n}$</font><font color=green>（复矩阵空间）上的内积</font>



- <mark>定义</mark>
  - $\begin{aligned}(A,B)&\triangleq tr(B^HA)=tr(AB^H)=\sum a_{ij}\overline{b_{ij}} ,A,B\in C^{m,n}\\(A,A)&\triangleq tr(A^HA)=tr(AA^H)=\sum a_{ij}\overline{a_{ij}} =\sum|a_{ij} |^2\end{aligned}$
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
  - $\begin{aligned}A^{H}& =\begin{pmatrix}\overline{a_{11}}&&\cdots&&\overline{a_{n1}}\\\vdots&&\ddots&&\vdots\\\overline{a_{1p}}&&\cdots&&\overline{a_{np}}\end{pmatrix} \in C^{p\times n} \\&=\begin{pmatrix}\overline{\alpha_1}^T\\\vdots\\\overline{\alpha_p}^T\end{pmatrix}\text{,其中}\overline{\alpha_1}^T\text{是}n\text{维行向量}1\times n\text{阶矩阵}\end{aligned}$
  - $\begin{aligned}A^{H}A& =\begin{pmatrix}\overline{\alpha_1}^T\\\vdots\\\overline{\alpha_p}^T\end{pmatrix}(\alpha_1,\cdots,\alpha_p) \\&=\begin{pmatrix}\overline{\alpha_1}^T\alpha_1&&\overline{\alpha_1}^T\alpha_2&&\cdots&\overline{\alpha_1}^T\alpha_p\\\overline{\alpha_2}^T\alpha_1&&\overline{\alpha_2}^T\alpha_2&&\cdots&\overline{\alpha_2}^T\alpha_p\\\vdots&&\vdots&&\ddots&\vdots\\\overline{\alpha_p}^T\alpha_1&&\overline{\alpha_p}^T\alpha_2&&\cdots&\overline{\alpha_p}^T\alpha_p\end{pmatrix} \\&=\begin{pmatrix}(\alpha_1,\alpha_1)&&(\alpha_2,\alpha_1)&&\cdots&&(\alpha_p,\alpha_1)\\(\alpha_1,\alpha_2)&&(\alpha_2,\alpha_2)&&\cdots&&(\alpha_p,\alpha_2)\\\vdots&&\vdots&&\ddots&&\vdots\\(\alpha_1,\alpha_p)&&(\alpha_2,\alpha_p)&&\cdots&&(\alpha_p,\alpha_p)\end{pmatrix} \\&=\begin{pmatrix}\overline{(\alpha_1,\alpha_1)}&&\overline{(\alpha_1,\alpha_2)}&&\cdots&&\overline{(\alpha_1,\alpha_p)}\\\overline{(\alpha_2,\alpha_1)}&&\overline{(\alpha_2,\alpha_2)}&&\cdots&&\overline{(\alpha_2,\alpha_p)}\\\vdots&&\vdots&&\ddots&&\vdots\\\overline{(\alpha_p,\alpha_1)}&&\frac{\vdots}{(\alpha_p,\alpha_2)}&&\cdots&&\overline{(\alpha_p,\alpha_p)}\end{pmatrix} \\&==\begin{pmatrix}|\alpha_1|^2&\overline{(\alpha_1,\alpha_2)}&\cdots&\overline{(\alpha_1,\alpha_p)}\\\overline{(\alpha_2,\alpha_1)}&|\alpha_2|^2&\cdots&\overline{(\alpha_2,\alpha_p)}\\\vdots&\vdots&\ddots&\vdots\\\overline{(\alpha_p,\alpha_1)}&\overline{(\alpha_p,\alpha_2)}&\cdots&|\alpha_\text{p}|^2\end{pmatrix}\end{aligned}$
---
## <font color=blue>正交</font>`<font color=codespan>orthogonal</font>`



### <font color=green>定义</font>



- $\begin{aligned}X\bot Y\iff(X,Y)=0& =x_1\overline{y_1} +x_2\overline{y_2} +\cdots+x_n\overline{y_n} \\&=\overline{\overline{x_1}\left.y_1\right.+\overline{x_2}\left.y_2\right.+\cdots+\overline{x_n}\left.y_n\right.} \\=(Y,X)\end{aligned}$
  >$X=\begin{pmatrix}x_{1}\\\vdots\\x_{n}\end{pmatrix}, Y=\begin{pmatrix}y_{1}\\\vdots\\y_{n}\end{pmatrix}\in\mathbf{C}^{n}$
### <font color=green>性质</font>



- $X\perp Y\iff\big(Y,X\big)=\overline{(X,Y)}=y_1\overline{x_1}+y_2\overline{x_2}+\cdots+y_n\overline{x_n}=0.$
- $X\perp Y\iff(Y,X)=0\iff(X,Y)=0$
- $X\perp Y\iff\mathrm{X}^HY=0\iff Y^HX=0$
  >$\mathrm{X}^{H}Y=(Y,X)=\overline{(X,Y)},\quad Y^{H}X=(X,Y)$
- $X\bot Y\Rightarrow aX\bot bY$
  >$(aX,bY)=\overline{b}Y^HaX=a\overline{b}Y^HX=a\overline{b}(X,Y)=0$
- $X_1\perp X_2\perp\cdots\perp X_n \\ \Rightarrow|c_1X_1\pm c_2X_2 \pm\cdots\pm c_nX_n|^2 =|c_1X_1|^2+ |c_2X_2|^2+\cdots+|c_nX_n|^2$
  >此时$X_1,X_2,\cdots,X_n$称为一个<strong>正交组</strong>
### <font color=green>tips</font>



- 零向量θ与任何向量均正交
- <strong>正交向量组</strong>要求向量均为<u>非零向量</u>
- <strong>正交向量组</strong><u>线性无关</u>
- 向量 $X$ 与 $Y$ 正交<strong>当且仅当</strong> <font color=red>$‖X+Y‖^2=‖X‖^2+‖Y‖^2$</font>
  >`勾股定理`
- 在 $n$ 维内积空间中，正交向量组中的向量个数不会超过n个
- 拓展
  ![](https://api2.mubu.com/v3/document_image/21954114_72b9b71b-8d0a-40b5-f894-754fbac171ba.png)
---
## <font color=blue>矩阵合同</font>



- 若$P^HAP=B(P可逆)$，则$A$与$B$ 合同，记为 $A\triangleq B$
### <font color=green>基本性质</font>



- <mark>对 称 性</mark> : $A\triangleq B\Longleftrightarrow B\triangleq A$
- <mark>传 递 性</mark> : $A\triangleq B， B\triangleq C\Longleftrightarrow A\triangleq C$
---
## <font color=blue>矩阵相似</font>



- <font color=green>定义</font>
- <font color=green>tips</font>
  - 两矩阵相似的<mark>充分必要条件</mark>是两矩阵的<strong>特征矩阵相抵</strong>
---
## <font color=blue>矩阵的秩</font>



- 矩阵秩越乘越小：<font color=red>$r(AB)<\rm min\{r(A),r(B)\}$</font>
- $\rm r(A)=r(AB)$ 成立的充要条件是存在适当阶数的矩阵$C$使得$ABC=A$
- 一般的，若$\rm (A-xI)(A-yI)=0$，则 $A$ 可以对角化
  - 例子 proof
    ![](https://api2.mubu.com/v3/document_image/21954114_fe70814f-609b-4103-c61c-2bf8c4fbe7d9.png)
- 对于任意 $n$ 阶矩阵 $A$，<font color=red>$\rm rank(A^n)=rank(A^{n+1})$</font>
- <strong>补充性质</strong>
  - 一些结论
    ![](https://api2.mubu.com/v3/document_image/21954114_122e0801-1bfd-4fec-fa55-a0600b62c588.png)
---
## <font color=blue>零化多项式</font>



### <font color=green>定义</font>



- 给定矩阵$A∈ℂ^{n×n}$
- 若存在多项式$g(λ)$使得$g(A)=0$
- 则称$g(λ)$为$A$的零化多项式
### <font color=green>性质</font>



- 复方阵A的零化多项式有无数个，A阵特征多项式的所有倍式都是A阵的零化多项式
---
## <font color=blue>首1多项式</font>



- 对于一元多项式 <font color=red>$g(λ)=a_nλ^n+a_{n−1}λ^n−1+⋯+a_1λ+a_0$</font>
- 如果 $a_n≠0$，则称 <font color=red>$a_nλ^n$</font>为多项式的<strong>首项</strong>
- $n$ 称为 $g(λ)$ 的次数，记为 <font color=red>$deg\big(g(λ)\big)=n$</font>
- $a_n$ 称为 $g(λ)$ 的首项系数
- 若<font color=red> </font><font color=red>$a_n=1$</font>，则称 $g(λ)$ 为<mark>首1多项式</mark>
---
## <font color=blue>最小多项式</font>



### <font color=green>定义</font>



- 复方阵 $A$ 的零化多项式中<strong>最小次数的</strong><font color=blue>首1多项式</font>称为矩阵A的最小多项式
- $m_A(λ)$
### <font color=green>性质</font>



- 矩阵A的最小多项式$m_A(λ)$是唯一的，且可整除矩阵A的任一零化多项式
  - 特别的 $m_A(λ) | f_A(λ)$
- 矩阵A的特征多项式$f_A(λ)$与最小多项式$m_A(λ)$具有<strong>相同的根（不计重数）</strong>
  - 矩阵A的最小多项式$m_A(λ)$必为特征多项式$f_A(λ)$的因式
  - 例子
    ![](https://api2.mubu.com/v3/document_image/21954114_ab164e7d-dcb5-4e3b-94aa-6434bd311229.png)
### <font color=green>求法</font>



- 利用Smith标准型求
- 利用特征多项式与定义求
- 利用Jordan标准型求
---
## <font color=blue>Jordan块</font>



>[参考](https://blog.csdn.net/qq_42192693/article/details/122248940)

### <font color=green>定义</font>



- <font color=red>Jordan块</font>
  ![](https://api2.mubu.com/v3/document_image/21954114_71a38d43-d51a-43e9-b870-650953477a34.png)
- <font color=red>Jordan标准形</font>
  ![](https://api2.mubu.com/v3/document_image/21954114_770ec21a-bc46-4c60-aa91-daba49d16d5c.png)
  - <font color=tag>例子</font>
    ![](https://api2.mubu.com/v3/document_image/21954114_e0f1b31d-fcec-46f7-bfdc-d1525a081411.png)
- <font color=green>Jordan标准形定理</font>
  - 设矩阵$J$是复方阵$A$的Jordan标准形，则矩阵$A$与矩阵$J$<strong>相似</strong>
  - <font color=tag>例子</font>
    - 题目
      ![](https://api2.mubu.com/v3/document_image/21954114_09e2cb3a-b0ca-4eda-e41b-f3e5c96b485b.png)
    - 解答
      ![](https://api2.mubu.com/v3/document_image/21954114_8154d4a6-5795-41f8-c441-792d34176ed9.png)
      ![](https://api2.mubu.com/v3/document_image/21954114_fcb1c144-4dc1-476a-9449-31427ed9c85a.png)
### <font color=green>性质</font>



- 任一Jordan块的<strong>最小多项式</strong>等于它的<strong>特征多项式</strong>，也是Jordan块<u>所对应特征矩阵的初等因子</u>
  - 给定初等因子所作的最简$\lambda$矩阵就是Jordan块的特征矩阵
- Jordan块本身就是一个Jordan矩阵
- <strong>对角阵</strong>是一个Jordan矩阵，它的每个Jordan块都是一阶的 $\Leftrightarrow$ A 的初等因子都是一次的
- Jordan标准型中，<strong>不同Jordan块的对角线元素可能相同</strong>，故特征值$\lambda_i$的代数重数 $\ge$ $\lambda_i$ 对应的某个Jordan块的阶数
- 矩阵不一定可以相似对角化，但一定可以与Jordan矩阵相似
### <font color=green>Jordan标准型求法</font>



- <mark>① 特征向量法</mark>
  - 如果 $\lambda_i$ 是 $A$ 的单重特征值，则 $\lambda_i$ 对应一阶Jordan块$\rm J_1(\lambda_i)$
  - 如果 $\lambda_i$ 是 $A$ 的 $r_i$ 重特征值（<mark>代数重数</mark>），设 $\rm s_i=dim(E_{\lambda_i})$
    >$E $ 指<font color=green>特征子空间</font>，$\rm dimE_{\lambda_i} = n-rank(A-\lambda_iI)$等于$\lambda_i$ 的几何重数
    - 则<strong>对应</strong> <strong>$\lambda_i$</strong> <strong>有</strong> <strong><font color=bold>$\rm s_i$</font></strong> <strong><font color=bold>个</font></strong> <strong>$\lambda_i$</strong><strong>为对角元的</strong><strong><font color=bold>Jordan块</font></strong>
    - 且这些Jordan块的<font color=red>阶数之和等于 </font><font color=red>$r_i$</font>
  - 由$A$的所有相异特征值对应的Jordan块构成的Jordan矩阵即为$A$的Jordan标准型
  - <font color=tag>例子</font>
    - ![](https://api2.mubu.com/v3/document_image/21954114_47761a55-261c-4628-8043-2c2ec61c0c4e.png)
- <mark>② 初等变换法</mark>
  - 方法一
    - 通过对$\lambda I-A$进行<strong>$\lambda$</strong><strong>矩阵的初等变换</strong>得到Smith标准型
    - 从而得到<strong>不变因子</strong>$\Rightarrow$<strong>初等因子</strong>$\Rightarrow$<strong>Jordan块</strong>
  - 方法二
    - 将$\lambda I-A$进行初等变换变成对角块矩阵
    - 直接得到初等因子，从而得到Jordan块
- <mark>③行列式因子法</mark>
  - 通过定义求$\lambda I-A$的<strong>行列式因子</strong>
  - 从而得到$\Rightarrow$<strong>不变因子</strong>$\Rightarrow$<strong>初等因子</strong>$\Rightarrow$<strong>Jordan块</strong>
### <font color=green>Jordan分解方法</font>



- <font color=tag>例子</font>
  - ![](https://api2.mubu.com/v3/document_image/21954114_4fb3176b-8604-413e-dc63-58ec1f4413b9.png)
  - ![](https://api2.mubu.com/v3/document_image/21954114_226a9773-1d98-4457-f479-19c72c690afc.png)
### <font color=green>Jordan标准型的幂</font>



- ![](https://api2.mubu.com/v3/document_image/21954114_b2d61761-a7f1-494d-b957-c86c75fa7307.png)
- ![](https://api2.mubu.com/v3/document_image/21954114_a1fd0cb4-eede-4fde-c0ce-76fedaf53c88.png)
- ![](https://api2.mubu.com/v3/document_image/21954114_702bd1f4-d182-40ca-f2b0-6c11a7a561bc.png)
### <font color=green>Jordan标准型求矩阵函数</font>



- $f(A) = P f(J)P^{-1}$
### <font color=green>tips</font>



- 利用Jordan标准型求矩阵最小多项式的方法
  - 单 Jordan 块情况
    - 当 $J$ 仅包含一个 Jordan 块 $J_1$ 时，$J_1$的最小多项式 $\rm m_{J_1}(\lambda)=(\lambda-\lambda_1)^{k_1}$
      - $\lambda_1$是 Jordan 块 $J_1$ 的特征值
      - $k_1$是 Jordan 块 $J_1$ 的阶数
  - 当 J 包含两个 Jordan 块 $J_1$ 和 $J_2$
    - 矩阵 $J$ 的最小多项式为$\rm m_{J_1}(\lambda)=(\lambda-\lambda_1)^{k_1}$和$\rm m_{J_2}(\lambda)=(\lambda-\lambda_2)^{k_2}$的<strong>最小公倍数</strong>
  - 一般的Jordan标准型 $J$
    - J 的<strong>最小多项式</strong>等于特征矩阵 $\rm \lambda I-A$ 的初等因子的最小公倍数，恰为<strong>不变因子</strong>$\rm d_n(\lambda)$
  - <font color=tag>例子</font>
    - ![](https://api2.mubu.com/v3/document_image/21954114_5993e512-568e-4676-8f9e-f6309370d450.png)
- 引理
  ![](https://api2.mubu.com/v3/document_image/21954114_796271b3-62fe-497d-ebf3-056df1705923.png)
---
## <font color=blue>映射、变换</font>



- 设 $V$ 和 $W$ 是两个非空集合，$f$ 是 $V$ 到 $W$ 的一个映射
### <font color=green>单射</font>



- 对任意 $x_1,x_2∈V$， 当 $x_1≠x_2$ 时有 $f(x_1)≠f(x_2)$
### <font color=green>满射</font>



- 对任意 $y∈W$ 都有一个元素 $x∈V$ 使得 $f(x)=y$
  >即存在原像
### <font color=green>双射</font>



- $f$ 既是单射，又是满射
  >即一一对应
### <font color=green>变换</font>



- 设 $V$ 是一个非空集合，<u>$V$</u><u> 到自身的映射</u>称为 $V$的<mark>变换</mark>
- V到自身的<u>双射</u>称为V的<mark>一一变换</mark>
- 若V是<u>有限集</u>，V的一一变换称为V的<mark>置换</mark>
### <font color=green>线性映射、线性变换</font>



- <strong>定义</strong>
  - 设 $V$ 和 $W$ 是数域 $F$ 上的线性空间，如果映射 <font color=red>$T:V→W$</font>满足下述性质，称 $T$ 为 $V$ 到 $W$ 的一个<strong>线性映射</strong>
    - <mark>可加性</mark>：$∀x,y∈V$ ，<font color=red>$T(x+y)=T(x)+T(y)$</font>
    - <mark>齐次性</mark>：$∀λ∈F$，<font color=red>$T(λx)=λT(x)$</font>
  - 特别的，当 $V=W$ 时， 称 $T$ 为 $V$ 上的<strong><u>线性变换</u></strong>
    - <strong>特殊的线性变换1</strong>
      >定义映射 $T:V→V$
      - <font color=red>零变换</font>：$T(x)=θ， ∀x∈V$
      - <font color=red>恒等变换</font>：$T(x)=x，∀x∈V$
      - <font color=red>负变换</font>：$T(x)=− x，∀x∈V$
    - <strong>特殊的线性变换2</strong>
      >定义 $T:ℝ^2→ℝ^2，∀x=[x_1,x_2]^T∈ℝ^2$​
      - <font color=red>伸缩</font>：$T(x)=\bigg[ \begin{matrix} k_1 & 0 \\ 0 & k_2 \end{matrix} \bigg]x$
        >$k_1$ 和$k_2$ 为正常数
        ​
      - <font color=red>反射</font>：$T(x)=(x_1,−x_2)$
      - <font color=red>旋转</font>：$T(x) = \bigg[ \begin{matrix} cos\varphi & -sin\varphi \\sin\varphi & cos\varphi \end{matrix}\bigg]x$
        >$\varphi$ 为旋转角
- <strong>关于线性映射的tips</strong>
  - <mark>定理 </mark>设$T$是数域 $F$上线性空间 $V$ 到 $W$的线性映射，若$α_1,⋯,α_p$是 $V$ 的一组向量，$k_1,\cdots,k_p \in F$
    - $T(k_1α_1+⋯+k_pα_p)=k_1T(α_1)+⋯+k_pT(α_p)$
  - <mark>推论 </mark>设$T$是数域 $F$上线性空间 $V$ 到 $W$的线性映射
    - <font color=red>$T(θ)=θ^′， θ∈V，θ^′∈W$</font>
      >几何意义——线性映射必须保持原点不动，故解析几何中常见的平移变换一般不是线性变换
    - <font color=red>$T(−x)=−T(x)，∀x∈V$</font>
    - 若 $α_1,⋯,α_p$ 是 $V$ 中一组<u>线性相关</u>向量, 则$T(α_1),⋯,T(α_p)$是$W$中一组<u>线性相关</u>向量
    - 若 $T(α_1),⋯,T(α_p)$ 是 $W$ 中一组<u>线性无关</u>向量，则 $α_1,⋯,α_p$ 是 $V$ 中一组<u>线性无关</u>向量
  - <mark>定理 </mark>设$T$是数域 $F$上 $n$ 维线性空间 $V$ 到 $m$ 维$W$的线性映射
    - 当且仅当 $T$ 是<strong>单射</strong>时，$V$中<strong>线性无关向量组</strong>的<strong><u>像</u></strong>是$W$中<strong>线性无关向量组</strong>
    - 当且仅当 $T$ 是<strong>单射</strong>时，$V$中<strong>一组基</strong>的<strong><u>像</u></strong>是 $W$ 中<strong>一组基</strong>。
      >此时映射 $T$ 是双射
  - 线性映射不一定将一组基映射为像空间的一组基
- <strong>关于线性变换的tips</strong>
  >设 $T$ 是线性空间 $V$ 的线性变换
  - 若 $T$ 可逆，则逆变换是线性变换
  - 若 $T$ 在欧式空间$V$ 的一组标准正交基 $x_1,\cdots,x_n$ 的矩阵是对称阵，则 $(T(x_i),x_j)=(x_i,T(x_j))$
- <strong>线性映射运算</strong>
  - 线性映射的<strong>加法</strong>运算
    - 设 $T_1, T_2\in \mathcal L(V,W)$，定义 $T_1$ 与 $T_2$ 的<mark>和</mark>为$\\$ <font color=red>$(T_1+T_2)(x)=T_1(x)+T_2(x)$</font>，$\forall x∈V$
  - 线性映射的<strong>数乘</strong>运算
    - 设$T\in \mathcal L(V,W)，\lambda \in F$， 定义 $λ$ 与 $T$ 的<mark>数乘</mark>为$\\$ <font color=red>$(\lambda T)( x)=\lambda\cdot T( x)$</font>，$\forall x∈V$
- <strong>线性映射空间、线性变换空间</strong>
  - 集合 $\mathcal L(V,W)$ 中赋以加法和数乘构成数域$F$上的线性空间，称为<font color=red>线性映射空间</font>
    - $\mathcal{L}(V,W)$表示线性空间V到W的所有线性映射的集合
  - 特别地，$\mathcal L(V)$称为<font color=red>线性变换空间</font>
  - <strong>注意</strong>：<font color=red>$\rm dim(\mathcal L(V,W)) = \rm dim(V) \times \rm dim(W)$</font>
- 线性映射<strong>值空间</strong>和<strong>核空间</strong>
  - <strong>定义</strong>
    - 设 $T \in \mathcal L(V,W)$
    - 线性映射$T$的<mark>核空间</mark> (零空间)
      - <font color=red>$N(T)=\{x∈V|T(x)=θ\}$</font>
    - $T$的<strong>零度</strong> (亏)
      - <font color=red>$\rm dim(N(T))$</font>
    - 线性映射$T$的<mark>值空间</mark>（像空间）
      - <font color=red>$R(T)=\{y∈W|y=T(x),∀x∈V\}$</font>
    - $T$的<strong>秩</strong>
      - <font color=red>$\rm dim(R(T))$</font>
  - <strong>性质</strong>
    - 设$V$和$W$是数域$F$上的$n$维和$m$维线性空间，若$T∈L(V,W)$在$V$的基$ε_1,⋯,ε_n$和$W$的基$η_1,⋯,η_m$下的矩阵为$A$
      - $\rm dimN(T)= dimN(A)$
      - $\rm dimR(T)=dimR(A)=rank(A)$
      - $\rm dimN(A)+dimR(A)=n$
- <strong>正交投影变换</strong>
  - 设 $W$ 是线性空间 $V$ 的<u>非平凡子空间</u>，定义 $V$ 上的<font color=red>正交投影变换</font>映射 $T$为
    >平凡子空间指零向量和自身
  - <font color=red>$T(x)=\mathrm{Proj_W}x$</font>
    > $∀x∈V$
  - 若$\alpha_1,\cdots,\alpha_p$ 为 $W$ 的<strong>标准正交基</strong>
    - $T(x)=\mathrm{Proj_W}x\\=(x,\alpha_1)\alpha_1+(x,\alpha_2)\alpha_2+\cdots+(x,\alpha_p)\alpha_p$
- <font color=blue>亏加秩定理</font>
### <font color=green>正交变换、酉变换</font>



- <strong>定义</strong>
  - 若<font color=red>欧氏</font> (<font color=purple>酉</font>)空间中的线性变换 $T$ <u>保持向量的内积不变</u>
  - $(T(x),T(y))=(x,y)，∀x,y∈V$
  - 称 $T$ 为<font color=red>正交</font>（<font color=purple>酉</font>）变换
- <strong>判定（充要条件）</strong>
  >设$V$是$n$维欧氏（酉）空间，$T∈\mathcal L(V)$
  - $T$保持长度不变，即 $\|T(x)\|=\|x\|$
  - 若 $ξ_1,⋯,ξ_n$ 是$V$ 中一组<strong>标准正交基</strong>，$\\$ 则$T(ξ_1),⋯,T(ξ_n)$ 也是$V$ 中一组<strong>标准正交基</strong>
  - $T$在$V$的任一标准正交基下的矩阵为正交（酉）矩阵
- <strong>性质</strong>
  - 正交变换保持两个向量的夹角不变
### <font color=green>同构映射</font>



- <strong>定义</strong>
  >其实就是`线性映射+双射`
  - 设$V$和$W$是数域$F$上的线性空间，$\forall x,y\in V$， $\forall λ\in F$
  - 存在<strong>双射</strong> $f:V→W$满足
    - （1）<font color=red>$f(x+y)=f(x)+f(y)$</font>
    - （2）<font color=red>$f(\lambda x)=\lambda f(x)$</font>
  - 则称线性空间$V$与$W$<mark>同构</mark>，$f$是$V$到$W$的<mark>同构映射</mark>
- <strong>性质</strong>
  >设V和W是数域F上的线性空间，T: V→W是同构映射
  - <font color=red>$T(\theta) = \theta^{\prime}$</font>，$\theta\in V,\theta^{\prime}\in W$
  - <font color=red>$T(-x)=-T(x)$</font>，$\forall x\in V$
  - <font color=red>$T(\sum\alpha_ix_i) = \sum \alpha_iT(x_i)$</font>，$\forall \alpha_i\in F,\forall x_i\in V$
  - $V$的向量组 $x_1,⋯,x_r$ <strong>线性相关</strong>当且仅当其像$T(x_1),⋯,T(x_r)$<strong>线性相关</strong>
  - 若 $ε_1,⋯,ε_n$ 是$V$的一组基，则$T(ε_1),⋯,T(ε_n)$是$W$的一组基
  - $T$的<strong>逆映射</strong>$T^{−1}: W→V$<strong>存在</strong>且是<strong>同构映射</strong>
- <strong>tips</strong>
  - 线性空间<strong>同构</strong><mark>当且仅当</mark>它们的<strong>维数相等</strong>
  - 任一实（复）$n$ 维线性空间均与 $\Bbb R^n（\Bbb C^n）$ 同构
  - 设$V$是数域 $\Bbb R（\Bbb C）$上的$n$维线性空间，则线性变换空间$L(V)$与 $\Bbb R^{n\times n}$（或 $\Bbb C^{n\times n}$）同构
### <font color=green>通过矩阵乘法实现线性映射</font>



- <strong>矩阵</strong>
  - ![](https://api2.mubu.com/v3/document_image/21954114_3591cd2b-e7c3-4b25-80e0-4e66b84753c3.png)
  - ![](https://api2.mubu.com/v3/document_image/21954114_7b6bc06b-6b09-40ec-ceed-ce0d6dbf7e92.png)
- <strong>线性映射与矩阵的关系</strong>
  - 示例
    ![](https://api2.mubu.com/v3/document_image/21954114_9f4c5a13-8b69-4a51-edb7-51feb60c0ee8.png)
- <strong>通过矩阵乘法实现线性映射</strong>
  - 设 $T\in \mathcal L(V,W)$，$T$在$V$的基$ε_1,⋯,ε_n$和$W$的基$η_1,⋯,η_m$下的矩阵为$A$。
    - $\Rightarrow$ <font color=red>$T(ε_1,⋯,ε_n)\\ \triangleq[T(ε_1),⋯,T(ε_n)]\\=[η_1,⋯,η_m]A$</font>
  - $\forall x\in V$，设
    - <font color=red>$x=[ε_1,⋯,ε_n] \alpha$</font>
    - <font color=red>$T(x)=[η_1,⋯,η_m]\beta$</font>
  - $\Rightarrow$ <font color=red>$\beta=A \alpha$</font>
- <strong>tips</strong>
  - 线性映射在不同基下的矩阵是相抵的
  - 推论
    - <font color=red>相似矩阵反映的是同一个线性变换</font>
      ![](https://api2.mubu.com/v3/document_image/21954114_bddb8abe-74ab-4ef1-d773-55e824490e76.png)

# <font color=purple>重要公式、定理</font>

---
## <font color=blue>许尔公式</font>



- $每个n 阶方阵\mathbf{A}=\mathbf{A}_{n\times n}\\ \text{都存在优阵 }\mathbf{Q}\\ \text{ 使得}\mathbf{Q}^{-1}\mathbf{A}\mathbf{Q}=\mathbf{D}=\begin{pmatrix}\lambda_1&\cdots&*\\&\ddots&\vdots\\0&&\lambda_n\end{pmatrix}\text{为上三角}$
- <mark>Schur引理</mark>
  >酉相似三角化
  - 任意复方阵$A$酉相似于上三角阵$\Lambda$
  - 即存在U阵 $U$ 使得 $U^HAU=Λ$
    - $U^HAU=Λ$
    - $Λ$——上三角矩阵
    - $U$——U阵
- <mark>实方阵Schur引理</mark>
  - 设$A∈ℝ^{n×n}$的特征值均为实数，则存在<strong>正交矩阵</strong> $Q$ 使得
    ![](https://api2.mubu.com/v3/document_image/21954114_7d62bc79-7b96-4cb1-f3ec-3ee780008f1f.png)
- <mark>tips</mark>
  - Schur引理表明任意复方阵都相似于<strong>上三角阵</strong>，但并不是所有复方阵都相似于对角阵
  - 可<mark>酉相似对角化</mark>的矩阵
    - 正规阵
      - Hermite阵、反Hermite阵、正交阵、酉矩阵等都是正规阵
    - Householder矩阵
  - 求Hermite矩阵$A$酉相似于对角阵的步骤
    - 求出A的全部相异特征值及重数
    - 对于每个特征值 $λ$，求方程$(λI−A)x=0$的一个基础解系，并将其单位正交化处理
    - 由标准正交特征向量生成酉矩阵$Q$，则$Q^TAQ$是对角矩阵
---
## <font color=blue>换位公式</font>



- ![](https://api2.mubu.com/v3/document_image/29f02167-2ac4-488f-bc58-bf085981538f.jpeg)
- ![](https://api2.mubu.com/v3/document_image/21954114_d1ff572c-9ade-486a-8551-8aaa1a03f551.png)
- ![](https://api2.mubu.com/v3/document_image/21954114_e7f5d0c0-6162-4fd5-9188-f6c2aa5ceb93.png)
- ![](https://api2.mubu.com/v3/document_image/21954114_bbb0e451-0403-49ee-a86d-885499c2a268.png)
---
## <font color=blue>特商公式</font>



- $\displaystyle\lambda=\frac{X^HAX}{|X|^2},\text{其中}(X\neq0\text{为}\lambda\text{的一个特征向量})$
  - $\text{证明}:X^HAX=X^H\lambda X=\lambda X^HX=\lambda|X|^2(|X|^2>0)$
---
## <font color=blue>平方公式</font>



- <mark>若 </mark>$A$ 为半正定（$A\ge 0$），或 $A$ 为正定（$A>0$）
- <mark>则有</mark>分解 $A=B^2$，且 $B^H=B$ 为<mark> </mark><mark>$Hermite$</mark><mark> 半正定</mark>（$B\ge0$）
- $B$ 叫 $A$ 的平方根，记作 $\displaystyle B=\sqrt{A}=A^{\frac12}$
---
## <font color=blue>秩公式</font>



- $r(AA^H)=r(A^HA)=r(A)$
---
## <font color=blue>亏加秩定理</font>



- 设T为数域F上的线性空间V到W的一个线性变换，即$T \in \mathcal{L}(V,W)$
- <font color=red>$\rm dimN(T)+dimR(T)=dimV$</font>
- 即线性映射 $T$ 的亏加秩等于其定义域 $V$ 空间的维数
---
## `<font color=codespan>Cayley</font>`<font color=blue>定理</font>



- $n$ 阶方阵的特征多项式 $T(x)=|xI-A|$ 也是它的一个 <font color=blue>零化多项式</font>，$\\$即有 $T(A)=0$
- 由该定理得到的有趣性质
  - 若$A\in C^{n\times n}$，则$A^n$一定可以由$A^{n-1},\cdots,A,I$线性表示，其中$n\geqslant2。$
- 例题
  - ![](https://api2.mubu.com/v3/document_image/21954114_6a512604-ef08-41ef-abb6-e741a72e2681.png)
---
## `<font color=codespan>Cauchy—Schwarz</font>`<font color=blue>不等式</font>



- <font color=green>定义</font>
  - 设$V$是数域$F$上的<strong>内积空间</strong>，对 $\forall x, y∈V$，有 <font color=red>$|(x,y)|≤‖x‖‖y‖$</font>
    - 注意：一般的线性空间不一定成立
  - 其中<strong>等号成立</strong>当仅当 <font color=red>$x, y$</font><font color=red>线性相关</font>
- <font color=green>三角不等式</font>
  - 设 $V$ 为欧式空间，则对任意的 $\alpha,\beta\in V$，有
  - $|\alpha+\beta|\le |\alpha|+|\beta|$
- <font color=green>拓展</font>
  >定义不同内积可得到不同的Cauchy不等式
  - 对 $ℝ^n$ 中任两向量 <mark>$x=[x_1,⋯,x_n]^T$</mark>和 <mark>$y=[y_1,⋯,y_n]^T$</mark>
    - $\displaystyle \left|\sum_{i=1}^nx_iy_i\right|\leq\sqrt{\sum_{i=1}^nx_i^2}\sqrt{\sum_{i=1}^ny_i^2}$
---
## `<font color=codespan>Holder</font>`<font color=blue>不等式</font>



- $\forall x=[x_1,x_2,\cdots,x_n]^T \in \Bbb C^n，y=[y_1,y_2,\cdots,y_n]^T \in \Bbb C^n$
- 设 <mark>$p,q>1$</mark>，且<mark>$\displaystyle \frac1p + \frac1q=1$</mark>
- <font color=red>$\displaystyle \sum_{i=1}^n|x_iy_i|\le \bigg(\sum_{i=1}^n |x_i|^p\bigg)^{\frac1p}\bigg(\sum_{i=1}^n |y_i|^q\bigg)^{\frac1q}$</font>
---
## `<font color=codespan>Minkowski</font>`<font color=blue>不等式</font>



- $\forall x=[x_1,x_2,\cdots,x_n]^T \in \Bbb C^n，y=[y_1,y_2,\cdots,y_n]^T \in \Bbb C^n$
- <mark>$p\ge1$</mark>
- <font color=red>$\displaystyle \bigg(\sum_{i=1}^n|x_i+y_i|^p \bigg)^{\frac1p}\le \bigg(\sum_{i=1}^n |x_i|^p\bigg)^{\frac1p}+\bigg(\sum_{i=1}^n |y_i|^p\bigg)^{\frac1p}$</font>



