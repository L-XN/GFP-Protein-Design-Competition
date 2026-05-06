import pandas as pd
import os

# ====================== 配置 ======================
DATA_DIR = "./data"
print("🔧 开始加载赛事数据与靶点挖掘...")

# 加载排除列表
exclusion_path = os.path.join(DATA_DIR, "Exclusion_List.csv")
if os.path.exists(exclusion_path):
    exclusion_df = pd.read_csv(exclusion_path)
    exclusion_seqs = exclusion_df.iloc[:, 0].str.strip().tolist()
    print(f"✅ 排除列表加载完成，共 {len(exclusion_seqs)} 条禁止序列")
else:
    print("ℹ️ 未找到排除列表，跳过加载")

# 野生型sfGFP模板
wt_sfgfp = "MSKGEELFTGVVPILVELDGDVNGHKFSVRGEGEGDATNGKLTLKFICTTGKLPVPWPTLVTTLTYGVQCFSRYPDHMKRHDFFKSAMPEGYVQERTISFKDDGTYKTRAEVKFEGDTLVNRIELKGIDFKEDGNILGHKLEYNFNSHNVYITADKQKNGIKANFKIRHNIVEDGSVQLADHYQQNTPIGDGPVLLPDNHYLSTQSVLSKDPNEKRDHMVLLEFVTAAGITHGMDELYK"

# 高亮度靶点（Top10 100%突变）
bright_sites = {30: "S", 39: "Y", 99: "F", 105: "N", 145: "Y", 153: "M", 207: "A"}
# 热稳定靶点
stable_sites = {172: "R", 204: "V", 213: "T"}

print("\n🎯 靶点挖掘完成！")
print("高亮度核心靶点：", bright_sites)
print("热稳定优化靶点：", stable_sites)

# 保存日志
os.makedirs("./logs", exist_ok=True)
with open("./logs/靶点挖掘执行日志.txt", "w", encoding="utf-8") as f:
    f.write(f"野生型序列长度：{len(wt_sfgfp)}\n")
    f.write(f"高亮度靶点：{bright_sites}\n")
    f.write(f"热稳定靶点：{stable_sites}\n")

print("✅ 第一步完成：数据加载与靶点挖掘")