from fpdf import FPDF, Align


class PDF(FPDF):
    # Constructor calls add_page() which calls header, then the user is prompted for their name and the shirt_text() method prints their name to the shirt.
    def __init__(self):
        super().__init__()
        self.add_page()
        self.image("shirtificate.png", x=Align.C, y=80)
        self.name = input("What is your name? ")
        self.shirt_text()
        
        
    def header(self):
        self.set_font("helvetica", "B", 36)
        self.cell(190, 60, "CS50 Shirtificate", align="C")
        
        
    def shirt_text(self):
        self.set_xy(28, 120)
        self.set_font_size(28)
        self.set_text_color(255)
        self.cell(160, 40, f"{self.name} took CS50", align="C")

# Creates a PDF object and outputs the PDF object as a .pdf file.                      
def main():
    pdf = PDF()
    pdf.output("shirtificate.pdf")
    
    
if __name__ == "__main__":
    main()