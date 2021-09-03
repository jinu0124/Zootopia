package ssafy;

import java.io.IOException;
import java.util.*;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class MatrixMulti {
	// Map
	public static class MMMapper extends Mapper<Object, Text, Text, Text>{
                private String Matrix1name;
                private String Matrix2name;

		private int n;	// number of rows in matrix A
		private int l;	// number of columns in matrix A
		private int m;	// number of columns matrix B
		protected void setup(Context context) throws IOException, InterruptedException {
			Configuration config = context.getConfiguration();
                        this.Matrix1name = config.get("Matrix1name");
			this.Matrix2name = config.get("Matrix2name");
			this.n = Integer.parseInt(config.get("n"));
			this.l = Integer.parseInt(config.get("l"));
			this.m = Integer.parseInt(config.get("m"));
			
		}

	        private Text location = new Text();
		private Text result = new Text();
		public void map(Object key, Text value, Context context
				) throws IOException, InterruptedException {
		    StringTokenizer st = new StringTokenizer(value.toString(), "\t");

		    while(st.hasMoreTokens()){
			String whichMat = st.nextToken();
			String x = st.nextToken();
			String y = st.nextToken();
			String val = st.nextToken();
		        if(whichMat.equals(Matrix1name)){
				for(int i=0; i<l; i++){
				    location.set(x + "," + i);
				    result.set(y + "," + val);

				    context.write(location, result);
				}
			}
			    else{
				for(int i=0; i<n; i++){
				    location.set(i + "," + y);
				    result.set(x + "," + val);

				    context.write(location, result);
				}
			    }
			
		    }
		}
	}
	// Reduce
	public static class MMReducer extends Reducer<Text, Text, Text, IntWritable> {
		private IntWritable val = new IntWritable();	// emit할 value로 사용할 변수
	    
	        private int n;	// number of rows in matrix A
	    	private int l;	// number of columns in matrix A
		private int m;	// number of columns matrix B
		protected void setup(Context context) throws IOException, InterruptedException {
			Configuration config = context.getConfiguration();
			this.n = Integer.parseInt(config.get("n"));
			this.l = Integer.parseInt(config.get("l"));
			this.m = Integer.parseInt(config.get("m"));
			
		}
	    private IntWritable result = new IntWritable();
		public void reduce(Text key, Iterable<Text> values, Context context) 
			throws IOException, InterruptedException {
		    
		    int min = m < (n < l ? n : l) ? m : (n < l ? n : l);
		    int[] mem = new int[min];
		    Arrays.fill(mem, 1);
		    for(Text value : values){
			String[] v = value.toString().split(",");
			mem[Integer.parseInt(v[0])] *= Integer.parseInt(v[1]);
		    }
		    int sum = 0;
		    for(int i=0; i<min; i++){
			sum += mem[i];
		    }
		   
		    result.set(sum);
		    context.write(key, result);
		}
	}
	// Main
	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
		if (otherArgs.length != 7) {
			System.err.println("Usage: <Matrix 1 name> <Matrix 2 name> <Number of row in Matrix 1><Number of columns in Matrix 1 (i.e., Number of rows in Matrix 2)> <Number of columns in Matrix 2> <in> <out>");
			System.exit(2);
		}

                FileSystem hdfs = FileSystem.get(conf);
                Path output = new Path(otherArgs[6]);
                if (hdfs.exists(output))
                        hdfs.delete(output, true);

		Job job = new Job(conf, "matrix multiplication prepare");
		Configuration config = job.getConfiguration();
                config.set("Matrix1name", otherArgs[0]);
                config.set("Matrix2name", otherArgs[1]);
		config.setInt("n",Integer.parseInt(otherArgs[2]));
		config.setInt("l",Integer.parseInt(otherArgs[3]));
		config.setInt("m",Integer.parseInt(otherArgs[4]));


		job.setJarByClass(MatrixMulti.class);
		job.setMapperClass(MMMapper.class);
		job.setReducerClass(MMReducer.class);
		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(Text.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		job.setNumReduceTasks(2);

		FileInputFormat.addInputPath(job, new Path(otherArgs[5]));
		FileOutputFormat.setOutputPath(job, new Path(otherArgs[6]));
		FileSystem.get(config).delete(new Path(otherArgs[1]),true);
		System.exit(job.waitForCompletion(true) ? 0 : 1);
	}
}
