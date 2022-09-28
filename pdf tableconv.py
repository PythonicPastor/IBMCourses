import tabula
import pandas
tabula.read_pdf("CEI-2022.pdf",pages="all")
tabula.convert_into("CEI-2022.pdf", "CEI.csv", output_format="csv", pages='all')
