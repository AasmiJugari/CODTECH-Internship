import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# ---------------------------
# READ DATA FROM FILE
# ---------------------------
data = pd.read_csv("data.csv")

# ---------------------------
# DATA ANALYSIS
# ---------------------------
average_marks = data["Marks"].mean()
highest_marks = data["Marks"].max()
lowest_marks = data["Marks"].min()

# ---------------------------
# CREATE PDF REPORT
# ---------------------------
file_name = "Student_Report.pdf"
pdf = canvas.Canvas(file_name, pagesize=A4)
width, height = A4

# Title
pdf.setFont("Helvetica-Bold", 16)
pdf.drawCentredString(width / 2, height - 50, "Student Performance Report")

# Content
pdf.setFont("Helvetica", 12)
y = height - 100

pdf.drawString(50, y, "Student Marks Data:")
y -= 30

for index, row in data.iterrows():
    pdf.drawString(60, y, f"{row['Name']} : {row['Marks']} marks")
    y -= 20

y -= 20
pdf.drawString(50, y, f"Average Marks: {average_marks:.2f}")
y -= 20
pdf.drawString(50, y, f"Highest Marks: {highest_marks}")
y -= 20
pdf.drawString(50, y, f"Lowest Marks: {lowest_marks}")

# Footer
pdf.setFont("Helvetica-Oblique", 10)
pdf.drawCentredString(width / 2, 30, "Generated Automatically Using Python")

# Save PDF
pdf.save()

print("PDF Report Generated Successfully!")
