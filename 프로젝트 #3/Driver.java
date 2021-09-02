package ssafy;

import org.apache.hadoop.util.ProgramDriver;

public class Driver {
	public static void main(String[] args) {
		int exitCode = -1;
		ProgramDriver pgd = new ProgramDriver();
		try {

			pgd.addClass("wordcount", Wordcount.class, "A map/reduce program that performs word counting.");
			pgd.addClass("wordcount1char", Wordcount1char.class, "A map/reduce program that performs word counting with char.");
			pgd.addClass("wordcountsort", Wordcountsort.class, "A map/reduce program with Partitioner Class");
			pgd.addClass("invertedindex", Wordcountsort.class, "A map/reduce program with Inverted Index");
			pgd.addClass("matrixadd", MatrixAdd.class, "A map/reduce program with Matrix addition");
      			pgd.driver(args);
			exitCode = 0;
		}
		catch(Throwable e) {
			e.printStackTrace();
		}

		System.exit(exitCode);
	}
}
