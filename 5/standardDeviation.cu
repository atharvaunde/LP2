#include<iostream>
using namespace std;

#define N 512


__global__ void Sum (int *a,int *o)
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

__global__ void standardDeviation(int *a,int avg)
{
  int tid = threadIdx.x;
  if(tid<N)
  {
    a[tid] -= avg;
    a[tid] = a[tid]*a[tid];
  }
}

int main()
{
    int *h_a,*d_a,*o_a,*oh_a,*d_a1;
    int size = N*sizeof(int);
    h_a = (int *)malloc(size);
    oh_a = (int *)malloc(size);

    cudaMalloc((void**)&d_a,size);
    cudaMalloc((void**)&o_a,size);
    //new
    cudaMalloc((void**)&d_a1,size);

    for(int i = 1; i <= N;i++)
    {
        h_a[i-1] = i;
    }


    cudaMemcpy(d_a,h_a,size,cudaMemcpyHostToDevice);
    cudaMemcpy(d_a1,h_a,size,cudaMemcpyHostToDevice);

    Sum<<<1,N/2>>>(d_a,o_a);

    cudaMemcpy(oh_a,o_a,size,cudaMemcpyDeviceToHost);

    int arithmetcMean = oh_a[0]/N;

    standardDeviation<<<1,N>>>(d_a1,arithmetcMean);

    Sum<<<1,N/2>>>(d_a1,o_a);

    cudaMemcpy(oh_a,o_a,size,cudaMemcpyDeviceToHost);

    int tmp = oh_a[0]/N;

    cout<<"Standard Deviation is - "<<sqrt(tmp)<<endl;

    cudaFree(d_a);
    free(h_a);
    cudaFree(o_a);
    free(oh_a);
    cudaFree(d_a1);
    
}

