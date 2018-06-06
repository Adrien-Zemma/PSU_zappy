NAME	= zappy_server

CC	= gcc

RM	= rm -f

SRCS	= ./server/srcs/accept.c \
	  ./server/srcs/commands/map_size.c \
	  ./server/srcs/commands.c \
	  ./server/srcs/getnextline.c \
	  ./server/srcs/main.c \
	  ./server/srcs/map.c \
	  ./server/srcs/parse.c \
	  ./server/srcs/read_command.c \
	  ./server/srcs/server.c \
	  ./server/srcs/set_socket.c \
	  ./server/srcs/utils.c 

OBJS	= $(SRCS:.c=.o)

CFLAGS = -I ./server/incs/
CFLAGS += -W -Wall -Wextra

all: $(NAME)

$(NAME): $(OBJS)
	 $(CC) $(OBJS) -o $(NAME) $(LDFLAGS)

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
