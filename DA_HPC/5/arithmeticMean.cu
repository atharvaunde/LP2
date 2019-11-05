#include<iostream>
using namespace std;

#define N 512


__global__ void ArithmeticMean (int *a,int *o)
{
    int of = N/2;

    int tid = threadIdx.x;

    for(of;of>0;of = of/2)
    {
        if(tid < of)
        {
            a[tid]+=a[tid+of];
        }
    }

    o[0] = a[0];
}

int main()
{
    int *h_a,*d_a,*o_a,*oh_a;
    int size = N*sizeof(int);
    h_a = (int *)malloc(size);
    oh_a = (int *)malloc(size);

    cudaMalloc((void**)&d_a,size);
    cudaMalloc((void**)&o_a,size);

    for(int i = 1; i <= N;i++)
    {
        h_a[i-1] = i;
    }


    cudaMemcpy(d_a,h_a,size,cudaMemcpyHostToDevice);

    ArithmeticMean<<<1,N/2>>>(d_a,o_a);

    cudaMemcpy(h_a,d_a,size,cudaMemcpyDeviceToHost);
    cudaMemcpy(oh_a,o_a,size,cudaMemcpyDeviceToHost);
    
    float AM =(float) oh_a[0]/N;
    cout<<"AM is "<<AM;

    cudaFree(d_a);
    free(h_a);
}

