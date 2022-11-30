import pandas as pd
import numpy as np
import seaborn as sns
# import matplotlib as plt #引入库的不同处，不能这样子写
import matplotlib.pyplot as plt
data = pd.read_excel(r'D:\desktop\train_data_2.xlsx')#r转义斜杠
# print(data)
# print(type(data))
# print("Pandas DataFrame:\n\n",data,"\n")
column = data.columns.tolist()[:5]
# print(type(column))
# print(column)
mcorr = data.corr('kendall')# 计算相关系数
print(mcorr)
mcorr_data = np.array(mcorr.activity)
# print(mcorr_data)
# # 返回上三角矩阵 只绘制下三角热力图
# mask = np.zeros_like(mcorr, dtype=bool)  # 构造与mcorr同维矩阵 为bool型
# mask[np.triu_indices_from(mask)] = True  # 角分线右侧为True
# 绘制图像
colors="Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, " \
       "Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, " \
       "Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, " \
       "PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r,RdYlBu, RdYlBu_r," \
       " RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, " \
       "Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, " \
       "autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm," \
       " coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray," \
       " gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern," \
       " gist_stern_r,gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r,hsv, " \
       "hsv_r, icefire,icefire_r, inferno,inferno_r, jet, jet_r, magma, magma_r, mako, mako_r, nipy_spectral," \
       " nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, " \
       "rocket, rocket_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, " \
       "tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, twilight, twilight_r, " \
       "twilight_shifted, twilight_shifted_r, viridis, viridis_r, vlag, vlag_r, winter, winter_r"
color=colors.split(',')
for i in color:
    i=i.strip()
    print(i)
    sns.heatmap(mcorr,
                annot=True,  # 显示相关系数的数据
                center=0.5,  # 居中
                fmt='.2f',  # 只显示两位小数
                linewidth=0.5,  # 设置每个单元格的距离
                linecolor='blue',  # 设置间距线的颜色
                vmin=0, vmax=1,  # 设置数值最小值和最大值
                xticklabels=True, yticklabels=True,  # 显示x轴和y轴
                square=True,  # 每个方格都是正方形
                cbar=True,  # 绘制颜色条
                cmap=f'{i}',  # 设置热力图颜色
                )
    plt.savefig('D:\desktop\photo\\'+f"{i}.png", dpi=600)  # 保存图片，分辨率为600
    plt.ion()  # 显示图片,这个可以方便后面自动关闭
    plt.pause(0.5)
    plt.close()#关闭图片

# plt.figure(figsize=(5, 5))
# cmap = sns.diverging_palette(220, 10, as_cmap=True)  # 返回matplotlib colormap对象
# # g = sns.heatmap(mcorr, mask=mask, cmap='coolwarm_r', square=True, annot=True, fmt='0.2f', center=0.5)  # 热力图，括号参数无顺序
# g = sns.heatmap(mcorr, cmap='coolwarm_r', square=True, annot=True, fmt='0.2f', center=0.5)  # 热力图，括号参数无顺序
# plt.savefig('D:\desktop\photo\\111', dpi=600)  # 保存图片，分辨率为600
# plt.show()

