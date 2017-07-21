f_ad<-file.choose(new = FALSE)
Data<-read.table(f_ad,sep="\t",head=T)
error<-c()
for(i in seq(0,1,0.0001))
{  error_P<-sum(Data$p<i)/length(Data$p)
  error<-c(error,error_P)
}
level<-seq(0,1,0.0001)
plot(level,error,xlab="Significance Level",ylab="Type I Error",ylim=c(0,1),pch=16)
dt<-data.frame(level,error)
write.table(dt, "TypeIerror.txt")
abline(a=0,b=1)

