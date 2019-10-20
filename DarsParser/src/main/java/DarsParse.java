import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.apache.pdfbox.cos.COSDocument;
import org.apache.pdfbox.io.RandomAccessFile;
import org.apache.pdfbox.io.RandomAccessRead;
import org.apache.pdfbox.pdfparser.PDFParser;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;

import java.io.*;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class DarsParse {
    private File inputPDF;
    private String DARPtext;
    ArrayList<String> completedClasses = new ArrayList<String>();
    ArrayList<String> selectClasses = new ArrayList<String>();
    Gson gson = new GsonBuilder().create();


    public DarsParse(File in) throws IOException {
        inputPDF = in;
        convertToText();
    }

    private void convertToText() throws IOException {

        PDFParser parser = null;
        PDDocument pdDoc = null;
        COSDocument cosDoc = null;
        PDFTextStripper pdfStripper;

        String parsedText = "";
        try {
            parser = new PDFParser(new RandomAccessFile(inputPDF, "r"));
            parser.parse();
            cosDoc = parser.getDocument();
            pdfStripper = new PDFTextStripper();
            pdDoc = new PDDocument(cosDoc);
            parsedText = pdfStripper.getText(pdDoc);
            //System.out.println(parsedText);
        } catch (Exception e) {
            e.printStackTrace();
            try {
                if (cosDoc != null)
                    cosDoc.close();
                if (pdDoc != null)
                    pdDoc.close();
            } catch (Exception e1) {
                e1.printStackTrace();
            }
        }

        DARPtext = parsedText;
        generateGSON();
    }

    public String getDARPtext() {
        return DARPtext;
    }

    private void generateGSON() throws IOException {
        //Pattern for completed courses
        Matcher getCompleted = Pattern.compile("[A-Z]{2}\\d{2}\\s([A-Z]+\\s\\d{3})").matcher(DARPtext);
        while(getCompleted.find()) {
            completedClasses.add(getCompleted.group(1));
        }
        Matcher getSelect = Pattern.compile("\\s[A-Z]{4}: ([A-Z]+ \\d+.+)").matcher(DARPtext);
        while(getSelect.find()) {
            selectClasses.add(getSelect.group(1));
        }
        System.out.print(DARPtext);

        Writer writer = new FileWriter("test.json");
        gson.toJson(completedClasses, writer);
        writer.close();

    }


    public static void main(String[] args) throws IOException {
        DarsParse convert = new DarsParse(new File("C:\\Users\\Quinn Collins\\Downloads\\Audit[213].pdf"));
    }
}