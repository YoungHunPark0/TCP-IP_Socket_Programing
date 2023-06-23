#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#define MAXBUF 1024
#define PORT 8080

char webpage[] = "HTTP/1.1 200 OK\r\n"
                "Server: Linux Web Server\r\n"
                "Content-Type: text/html; charset=UTF-8\r\n\r\n"
                "<!DOCTYPE html>\r\n"
                "<html><head><title>My Web Page</title>\r\n"
                "<style>body {background-color: #FFFF00;}</style></head>\r\n"
                "<body><center><h1>Hello World!!</h1><br>\r\n"
                "<img src=\"hedgehog.jpg\"></center></body></html>\r\n";

int main()
{
    int socket_desc, client_sock, c;
    struct sockaddr_in server, client;
    char client_message[MAXBUF];

    // 소켓 생성
    socket_desc = socket(AF_INET, SOCK_STREAM, 0);
    if (socket_desc == -1)
    {
        printf("Could not create socket");
        return 1;
    }

    // 서버 주소 설정
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(PORT);

    // 소켓 바인딩
    if (bind(socket_desc, (struct sockaddr *)&server, sizeof(server)) < 0)
    {
        perror("bind failed");
        return 1;
    }
    printf("Bind done\n");

    // 클라이언트의 연결 요청 대기
    listen(socket_desc, 3);

    printf("Waiting for incoming connections...\n");

    c = sizeof(struct sockaddr_in);

    // 클라이언트의 연결 수락
    client_sock = accept(socket_desc, (struct sockaddr *)&client, (socklen_t *)&c);
    if (client_sock < 0)
    {
        perror("accept failed");
        return 1;
    }
    printf("Connection accepted\n");

    // 클라이언트로부터 데이터 수신
    if (recv(client_sock, client_message, MAXBUF, 0) < 0)
    {
        perror("recv failed");
        return 1;
    }
    printf("Received message:\n%s\n", client_message);

    // 웹페이지 응답 전송
    if (send(client_sock, webpage, strlen(webpage), 0) < 0)
    {
        perror("send failed");
        return 1;
    }
    printf("Webpage sent\n");

    // 소켓 종료
    close(client_sock);
    close(socket_desc);

    return 0;
}
