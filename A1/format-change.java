package accuracy;

import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.io.FileWriter;

public class filereader {
	public static void main(String[] args) {
		try{
			
			//file one
			FileReader fr = new FileReader("Input/Output.txt");
			BufferedReader br = new BufferedReader(fr);
			String line;
			int numberOfLines =0;
			ArrayList<String[]> x = new ArrayList<String[]>();
			
			while((line = br.readLine()) != null)
			{
				
				
				String[] temp_string = line.split("\\t+");
				/*//to split a text by underline
				for(int i=0; i<temp_string.length;i++){
					String[] temp_string2 = temp_string[i].split("\\_");
					x.add(temp_string2);
				}*/
				
				//System.out.println(line);
				//for(int i=0; i<temp_string.length; i++){
					//if(temp_string[i] != "\\n"){
						//x.add(temp_string);
					//}
				//}
				x.add(temp_string);
				//System.out.println("********");
				numberOfLines++;
			}
			System.out.println("Number of lines: " + numberOfLines);
			
			
			br.close();
			fr.close();
			
			ArrayList<String> string_name = new ArrayList<String>();
			ArrayList<String> string_tag = new ArrayList<String>();
			//print array of first file
			int NumberOfTokens=0;
			for (int i=0;i<x.size(); i++){
				for(int i2=0; i2<x.get(i).length; i2++){
					if(x.get(i)[i2].equals(x.get(1)[0])){
						
							string_name.add("Separator");
							string_tag.add("Separator");
					}
						else{
							if(i2==0){
							string_name.add(x.get(i)[i2]);}
							else{ 
								string_tag.add(x.get(i)[i2]);
							}
							//System.out.println("******");
							//System.out.println(x.get(i)[i2]);
							//System.out.println("******");
					NumberOfTokens++;
					}
				}
			}
			System.out.println("number of tokens and tags: " +NumberOfTokens);
			
			int Ntag=0;
			for (int i=0;i<string_name.size(); i++){
				for(int j=0; j<string_tag.size(); j++){
				
				if(i == j){
					if (string_name.get(i).equals("Separator") && string_tag.get(j).equals("Separator")){
						System.out.println("");
						break;
					}
				System.out.printf(string_name.get(i) + "_" + string_tag.get(j) + " ");
				Ntag++;
				}
				}
			}
			System.out.println("\nnumber of tags: " + Ntag);
			System.out.println("number of tokens and tags: " +NumberOfTokens);
			
			
			String output = "";
					for (int i=0;i<string_name.size(); i++){
						for(int j=0; j<string_tag.size(); j++){
						
						if(i == j){
							if (string_name.get(i).equals("Separator") && string_tag.get(j).equals("Separator")){
								output +="\n";
								break;
							}
						 output += string_name.get(i) + "_" + string_tag.get(j) + " ";
						
						}
						}
					}
			String filename = "Output/test2.txt" ;
	        FileWriter filewriter = new FileWriter(filename);
	        BufferedWriter bufferedwriter = new BufferedWriter(filewriter);
	        bufferedwriter.write(output);
	        bufferedwriter.close();
			
		}catch (IOException e)
		{
			e.printStackTrace();
		}

}
}

