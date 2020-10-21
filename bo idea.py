#include<stdio.h>
#include<math.h> 
#include<stdlib.h>
int main()
{ 
	int num;
	int array[100][100];
	int count=0;
	int i,j;
	int rt; 
	float sq=0;
	scanf("%d\n", &num);
	for(i=0;i<num;i++) {
		for(j=0; j<num; j++) { 
			scanf("%d ", & array[i][j]);
		}
	} 
	for(i=0;i<num; i++) {
		for (j=0;j<num;j++) {
			if(array[i][j]=='D') {
				count=count+1;
			}
		}
	}
	sq=sqrt(count); 
	rt=floor(sq); 
	for(i=0;i<num; i++){
		for(j=0; j<num; j++){
			printf("%d ",rt);
		}
	}
	return 0;
}