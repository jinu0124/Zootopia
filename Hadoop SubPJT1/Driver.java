package ssafy;

import org.apache.hadoop.util.ProgramDriver;

public class Driver {
	public static void main(String[] args) {
		int exitCode = -1;
		ProgramDriver pgd = new ProgramDriver();
		try {
		    pgd.addClass("wordcount", Wordcount.class, "wordcount");
		    pgd.addClass("wordcount1char", Wordcount1char.class, "wordcount1char");
		     pgd.addClass("wordcountPart", Wordcountpart.class, "wordcount1char");
			pgd.addClass("inverted", InvertedIndex.class, "inverted index");
			pgd.addClass("matrixadd", MatrixAdd.class, "matrix add");
			pgd.addClass("matrixmulti", MatrixMulti.class, "matrix multi 1-phase.");
      			pgd.driver(args);
			exitCode = 0;
		}
		catch(Throwable e) {
			e.printStackTrace();
		}

		System.exit(exitCode);
	}
}
