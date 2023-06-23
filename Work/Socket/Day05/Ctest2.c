#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

#define PORT 8080
#define MAX_BUFFER_SIZE 50000

char webpage[] = "HTTP/1.1 200 OK\r\n"
                 "Server: Linux Web Server\r\n"
                 "Content-Type: text/html; charset=UTF-8\r\n\r\n"
                 "<!DOCTYPE html>\r\n"
                 "<html><head><title> My Web Page </title>\r\n"
                 "<style>body {background-color: #FFFF00 }</style><head>\r\n"
                 "<body><center><h1>Hello World!!</h1><br>\r\n"
                 "<img src=\"hedgehog.jpg\"></center></body></html>\r\n";

int main() {
    int server_fd, new_socket, valread;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[MAX_BUFFER_SIZE] = {0};

    // 소켓 생성
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("소켓 생성 실패");
        exit(EXIT_FAILURE);
    }

    // 소켓 옵션 설정
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt))) {
        perror("소켓 옵션 설정 실패");
        exit(EXIT_FAILURE);
    }

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // 소켓에 주소 바인딩
    if (bind(server_fd, (struct sockaddr*)&address, sizeof(address)) < 0) {
        perror("바인딩 실패");
        exit(EXIT_FAILURE);
    }

    // 클라이언트의 연결 요청 대기
    if (listen(server_fd, 3) < 0) {
        perror("대기 실패");
        exit(EXIT_FAILURE);
    }

    printf("웹 서버 실행 중...\n");

    while (1) {
        // 클라이언트의 연결 수락
        if ((new_socket = accept(server_fd, (struct sockaddr*)&address, (socklen_t*)&addrlen)) < 0) {
            perror("연결 수락 실패");
            exit(EXIT_FAILURE);
        }

        // 클라이언트로부터 데이터 수신
        valread = read(new_socket, buffer, MAX_BUFFER_SIZE);

        // GET/POST 요청에 따라 응답 전송
        if (strstr(buffer, "GET /") != NULL || strstr(buffer, "POST /") != NULL) {
            write(new_socket, webpage, strlen(webpage));
        }

        // 연결 종료
        close(new_socket);
    }

    // 소켓 종료
    close(server_fd);

    return 0;
}
