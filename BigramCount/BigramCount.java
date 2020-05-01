// Modified from Apache Hadoop's starter code at the link:
// https://hadoop.apache.org/docs/r1.2.1/mapred_tutorial.html

import java.io.IOException;
import java.util.*;
	
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;
	
public class BigramCount {
	
   public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, Text, IntWritable> {
     private final static IntWritable one = new IntWritable(1);
     private Text bigram = new Text();
     // To construct the bigrams, we store previous and current words
     private String prevToken = null;
     private String currToken = null;

     public void map(LongWritable key, Text value, OutputCollector<Text, IntWritable> output, Reporter reporter) throws IOException {
       String line = value.toString();
       StringTokenizer tokenizer = new StringTokenizer(line);
       // Loop through all of the words
       while (tokenizer.hasMoreTokens()) {
	 // Get the current word
         currToken = tokenizer.nextToken();
	 // Only construct bigrams if the current word has a previous word
	 if (prevToken != null) {
	   // Combine the previous word with the current word to construct a bigram
           bigram.set(prevToken + " " + currToken);
           output.collect(bigram, one);
	 }
	 // Update the previous word and restart loop
	 prevToken = currToken;
       }
     }
   }

   public static class Reduce extends MapReduceBase implements Reducer<Text, IntWritable, Text, IntWritable> {
     public void reduce(Text key, Iterator<IntWritable> values, OutputCollector<Text, IntWritable> output, Reporter reporter) throws IOException {
       int sum = 0;
       while (values.hasNext()) {
         sum += values.next().get();
       }
       output.collect(key, new IntWritable(sum));
     }
   }

   public static void main(String[] args) throws Exception {
     JobConf conf = new JobConf(WordCount.class);
     conf.setJobName("bigramcount");

     conf.setOutputKeyClass(Text.class);
     conf.setOutputValueClass(IntWritable.class);

     conf.setMapperClass(Map.class);
     conf.setCombinerClass(Reduce.class);
     conf.setReducerClass(Reduce.class);

     conf.setInputFormat(TextInputFormat.class);
     conf.setOutputFormat(TextOutputFormat.class);

     // Set the number of reducer tasks to 5
     conf.setNumReduceTasks(5);

     FileInputFormat.setInputPaths(conf, new Path(args[0]));
     FileOutputFormat.setOutputPath(conf, new Path(args[1]));

     JobClient.runJob(conf);
   }
}

