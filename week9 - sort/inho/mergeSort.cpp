#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> array = {10, 40, 90, 30, 20, 67, 89};

void merge(int left, int mid, int right){
    // 새로 합칠 배열을 만든다음에
    vector<int> sorted(array.size());
    
    // 기존 array 값 참고해서 채우고
    int i = left;
    int j = mid + 1;
    int tmp = left;
    while(i <= mid and j <= right){
        if(array[i] <= array[j]){
            sorted[tmp++] = array[i++];
        }else{
            sorted[tmp++] = array[j++];
        }
    }
    
    while(i <= mid){
        sorted[tmp++] = array[i++];
    }
    while(j <= right){
        sorted[tmp++] = array[j++];
    }
    
    
    // 마지막에 array에 덮어쓰기
    for(int k = left; k <= right; k++){
        array[k] = sorted[k];
    }
}

void mergeSort(int left, int right){
    if(left >= right) return;
    
    int mid = (left + right) / 2;
    mergeSort(left, mid);
    mergeSort(mid + 1, right);
    merge(left, mid, right);
}

int main() {
    mergeSort(0, array.size()-1);
    for(int i: array){
        cout << i << endl;
    }

    return 0;
}