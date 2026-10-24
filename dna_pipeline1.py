from Bio import Entrez
from Bio import SeqIO
import pandas as pd
import matplotlib.pyplot as plt

# 1. Database Identification Protocols
Entrez.email = "ijlal.muneer@studentmail.com" # Authenticating with NCBI servers
print("🚀 Reaching out to global databases to harvest radiation-resistant material...")

# Fetching the DNA damage repair protein RecA from Deinococcus radiodurans
# Accession ID AE000513 represents this extremophile's primary repair engine genomic segment
handle = Entrez.efetch(db="nucleotide", id="AE000513", rettype="fasta", retmode="text")
space_record = SeqIO.read(handle, "fasta")
handle.close()

space_dna = space_record.seq
total_length = len(space_dna)

# 2. Advanced Landscape Matrix Calculations
g_count = space_dna.count('G')
c_count = space_dna.count('C')
gc_content = (g_count + c_count) / total_length * 100

print("\n--- COSMIC SHIELDING ANALYTICS TARGET REPORT ---")
print(f"📌 Organism Target: {space_record.description[:65]}...")
print(f"🧬 Analyzed Window: {total_length:,} base pairs")
print(f"🌡️ Global GC Density: {gc_content:.2f}%")

# 3. Running Systems Logic Check on Radiation Survival
# Extremophiles often favor incredibly high GC content because the triple hydrogen bonds 
# provide exceptional structural integrity against cosmic rays, preventing molecular fracturing.
print("\n--- BIO-STRUCTURAL PREDICTIVE VERDICT ---")
if gc_content > 60:
    print(f"🟢 VERDICT: HIGH COSMIC DEFENSE PROFILE ({gc_content:.2f}%)")
    print("   Structural Architecture Evaluation: The high density of triple hydrogen bonds")
    print("   provides extreme thermal and physical shielding against radiation fractures.")
else:
    print("🟡 VERDICT: BASAL PROFILE. Standard terrestrial vulnerability patterns detected.")

# 4. Compiling the Digital Corporate Asset
metrics_df = pd.DataFrame({
    'Metric Parameter': ['Total Length', 'GC Percentage', 'AT Percentage'],
    'Value Field': [f"{total_length:,} bp", f"{gc_content:.2f}%", f"{(100 - gc_content):.2f}%"]
})
metrics_df.to_csv("space_biology_shielding_metrics.csv", index=False)
print("\n💾 PIPELINE STATUS: Spreadsheet compiled and saved as 'space_biology_shielding_metrics.csv'!")
