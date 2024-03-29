# Part II

We've talked about how Hadoop works, you've seen Hadoop code, and you've written some code of your own using our store sales data. Now we'd like you to solve some problems using a different dataset on your own. You'll have to write your Mappers and Reducers from scratch; please use Python. You will have to do the data processing on your local pseudo-distributed cluster, but you will be able to see if your solution was correct by submitting your results to our system.

The data set we're using is an anonymized Web server log file from a public relations company whose clients were DVD distributors. The log file is in the udacity_training/data directory, and it's currently compressed using GnuZip. So you'll need to decompress it and then put it in HDFS. If you take a look at the file, you'll see that each line represents a hit to the Web server. It includes the IP address which accessed the site, the date and time of the access, and the name of the page which was visited.

######The logfile is in Common Log Format:

    10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
    %h%l %u %t \"%r\" %>s %b
    
    


######Where:
* **%h** is the IP address of the client
* **%l** is identity of the client, or "-" if it's unavailable
* **%u** is username of the client, or "-" if it's unavailable
* **%t** is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]
* **%r** is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.
* **%>s** is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found). See more information on status codes in W3C.org
* **%b** is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.
 

For each of the problems, we would like you to write a MapReduce job to solve the problem and when you have done that you should be able to answer the question we are going to ask you.



### Excercises
* **Problem Set 1** = Write a MapReduce program which will display the number of hits for each different file on the Web site.
                  (Example: How many hits were made to the page: "/assets/js/the-associates.js")
* **Problem Set 2** = Write a MapReduce program which determines the number of hits to the site made by each different IP address.
                  (Example: How many hits were made by the IP address: "10.99.99.186")
* **Problem Set 3** = Find the most popular file on the Web site. In other words, the file which had the most hit. Your Reducer                       should just write out the name of the file and the number of hits into HDFS.
                  (Example: Full path to the most popular file, Number of hits to that file)



