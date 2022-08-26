/*
    AUTHOR: Ved J Nayi
    DOC: 18-08-22
    Objective: a function insatind(array,position,element) to insert an element into an array
               at the specified index (position).
*/
#include<stdio.h>

#define size 5

void insatind(int arr[],int pos,int ele);

int main()
{
    int a[50],pos,num,i;

    for(i=0;i<size;i++)
    {
        printf("\na[%d]: ",i);
        scanf("%d",&a[i]);
    } // end of scanning
    
    printf("\nEnter position to insert: ");
    scanf("%d",&pos);
    printf("\nEnter element to enter: ");
    scanf("%d",&num);

    insatind(a,pos,num);
    return 0;
}

void insatind(int arr[],int pos,int ele)
{
    int i;
    for(i=size-1;i>=pos-1;i--)
    {
        arr[i+1] = arr[i];
    }
    arr[pos-1] = ele;

    for(i=0;i<size+1;i++)
    {
        printf("%d ",arr[i]);
    }
}