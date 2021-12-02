package excelExportAndFileIO;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class ExcelFile {
	
	public Sheet readExcel(String filePath,String fileName,String sheetName) throws IOException{
		File file =	new File("C://Software//Keyword Driven Framework//KeywordDrivenFramework//TestCase.xlsx");
		FileInputStream inputStream = new FileInputStream(file);
		Workbook sbWorkbook = null;
		String fileExtensionName = fileName.substring(fileName.indexOf("."));
		//Check condition if the file is xlsx file
		if(fileExtensionName.equals(".xlsx")){
		sbWorkbook = new XSSFWorkbook(inputStream);
		}
		else if(fileExtensionName.equals(".xlsx")){
			sbWorkbook = new HSSFWorkbook(inputStream);
		}
		Sheet  sbSheet = sbWorkbook.getSheet(sheetName);
		 return sbSheet;	
		}
	}




