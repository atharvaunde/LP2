#include <stdio.h>
#include <stdlib.h>
#include <cuda.h>

#define n 512

__global__ void bmk_add(int *a, int *b, int *result)
{
	int i = threadIdx.x;
	result[i] = a[i] + b[i];
}

int main()
{
	int num_blocks = 1, num_threads = n;

	int *a, *b, *c;
	int *dev_a, *dev_b, *dev_c;

	int size = n * sizeof(int);

	a = (int*)malloc(size);
	b = (int*)malloc(size);
	c = (int*)malloc(size);

	cudaMalloc((void**)&dev_a,size);
	cudaMalloc((void**)&dev_b,size);
	cudaMalloc((void**)&dev_c,size);

	for(int i = 0;i<n;i++)
	{
		//a[i] = rand()%1024;
		//b[i] = rand()%1024;
		a[i] = i;
		b[i] = i;
	}

	cudaMemcpy(dev_a,a,size,cudaMemcpyHostToDevice);
	cudaMemcpy(dev_b,b,size,cudaMemcpyHostToDevice);

	bmk_add <<<num_blocks, num_threads>>>(dev_a,dev_b,dev_c);

	cudaMemcpy(c,dev_c,size,cudaMemcpyDeviceToHost);

	for(int i = 0;i<n;i++)
		printf("%d  ",c[i]);
    
    printf("\n");
	cudaFree(dev_a);
	cudaFree(dev_b);
	cudaFree(dev_c);

	return 0;
}
