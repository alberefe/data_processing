FROM golang:1.24.3-bookworm

WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN go build -o main .

CMD ["./main"]