#include <string>
#include <iostream>
#include <vector>

using namespace std;
vector<int> values = {80, 90, 30, 40, 60, 70};

void swap(int a, int b){
    int tmp = values[a];
    values[a] = values[b];
    values[b] = tmp;
}

int partition(int left, int right){
    int mid = (left + right) / 2;
    swap(left, mid);
    
    int pivot = values[left];
    
    int i = left;
    int j = right;
    
    while(i < j){
        while(pivot < values[j]){
            j--;
        }
        
        while(i < j and pivot >= values[i]){
            i++;
        }
        
        swap(i, j);
    }
    values[left] = values[i];
    values[i] = pivot;
    return i;
}

void quickSort(int left, int right){
    if(left >= right) return;
    
    int pivot = partition(left, right);
    quickSort(left, pivot - 1);
    quickSort(pivot + 1, right);
}

int main() {
    quickSort(0, values.size()-1);
    
    for(int i : values){
        cout << i << endl;
    }

    return 0;
}

