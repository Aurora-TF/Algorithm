#include <string>
#include <vector>
#include <stack>
using namespace std;

struct Node{
    Node* prev;
    Node* next;
    int index;
    Node(Node* prev, Node* next, int index) : prev(prev), next(next), index(index)  {}
};
// n = 1,000,000
// x = 300,000 //x 합 1,000,000 이하
// cmd = 200,000
// 일반 배열로 풀면
// 이동에 O(n) (삭제유무확인후 이동수 확인해야함)
// 삭제에 O(n) (삭제 후 커서이동에 삭제유무 확인)
// 복구에 O(1)

// 더블링크드리스트로 풀면
// 이동에 O(x)
// 삭제에 O(1)
// 복구에 O(1)


string solution(int n, int k, vector<string> cmd) {
    string answer(n, 'O');
    Node* head = new Node(nullptr, nullptr, -1);
    Node* cur = head;
    Node* kur;
    
    for(int i=0; i<n; i++){
        Node* tmp = new Node(cur, nullptr, i);
        cur->next = tmp;
        cur = tmp;
        if(i == k) kur = tmp;
    }
    
    Node* tail = new Node(cur, nullptr, -2);
    cur->next = tail;
    
    stack<Node*> del;
    int moveCnt = 0;
    for(string c : cmd){
        switch(c[0]){
            case 'D':
                moveCnt = stoi(c.substr(2));
                for(int i=0; i<moveCnt; i++){
                    kur = kur->next;
                }
                break;
            case 'C':
                del.push(kur);
                answer[kur->index] = 'X';
                kur->prev->next = kur->next;
                kur->next->prev = kur->prev;
                kur = (kur->next == tail) ? kur->prev : kur->next;
                break;
            case 'U':
                moveCnt = stoi(c.substr(2));
                for(int i=0; i<moveCnt; i++){
                    kur = kur->prev;
                }
                break;
            case 'Z':
                Node* delNode = del.top();
                del.pop();
                answer[delNode->index] = 'O';
                delNode->prev->next = delNode;
                delNode->next->prev = delNode;
                break;
                
        }
        
    }
    
    return answer;
}