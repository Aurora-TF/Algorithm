#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

// 어떤 문자열이 다른 문자열의 첫번째부터 포함되는지를 알아야하는데
// 먼가 트라이 알고리즘 같기도하고
// 루트부터 숫자 10가지로 뻗어나가는 트리를 만들고
// 내가 마지막노드면 표시
// 다음 문자열에서 똑같이 뻗어나가다가 마지막노드라고 표시된 경우 중복이 있는거니까 바로 false 반환

struct Node {
    bool isLastNumber;
    Node* next[10];
};

bool solution(vector<string> phone_book) {
    bool answer = true;
    Node* root = new Node();
    sort(phone_book.begin(), phone_book.end());
    
    for(string number : phone_book){
        Node* tmp = root;
        for(int i=0; i<number.size(); i++){
            char n = number[i];
            int index = n - '0';
            if(tmp->next[index] == nullptr){
                tmp->next[index] = new Node();
            }
            if(tmp->next[index]->isLastNumber){
                return false;
            }
            
            if(i == number.size()-1){
                tmp->next[index]->isLastNumber = true;
            }
            tmp = tmp->next[index];
        }
    }
    return answer;
}