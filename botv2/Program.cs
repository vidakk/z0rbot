using System;
using System.Linq;
using System.Threading.Tasks;
using Discord;
using Discord.WebSocket;
using Microsoft.Extensions.Configuration;
using System.IO;

class Program
{
    private DiscordSocketClient? _client;
    private string? _botChannel;
    private readonly Random _random = new Random();

    static void Main(string[] args) => new Program().MainAsync().GetAwaiter().GetResult();

    public async Task MainAsync()
    {
        var config = new ConfigurationBuilder()
            .SetBasePath(Directory.GetCurrentDirectory())
            .AddJsonFile("appsettings.json")
            .AddEnvironmentVariables()
            .Build();

        var discordToken = config["DISCORD_TOKEN"];
        _botChannel = config["DISCORD_BOT_CHANNEL"];

        var socketConfig = new DiscordSocketConfig
        {
            GatewayIntents = GatewayIntents.Guilds | GatewayIntents.GuildMessages | GatewayIntents.MessageContent
        };

        _client = new DiscordSocketClient(socketConfig);
        _client.Log += Log;
        _client.MessageReceived += MessageReceivedAsync;
        _client.Ready += ReadyAsync;

        await _client.LoginAsync(TokenType.Bot, discordToken);
        await _client.StartAsync();

        await Task.Delay(-1);
    }

    private Task Log(LogMessage msg)
    {
        Console.WriteLine(msg.ToString());
        return Task.CompletedTask;
    }

    private Task ReadyAsync()
    {
        Console.WriteLine($"Logged in as {_client!.CurrentUser}");
        return Task.CompletedTask;
    }

    private async Task MessageReceivedAsync(SocketMessage message)
    {
        if (message.Author.Id == _client!.CurrentUser.Id)
            return;

        var channel = _client.GetChannel(message.Channel.Id) as ISocketMessageChannel;
        var c_channel = _client.Guilds.SelectMany(g => g.TextChannels).FirstOrDefault(c => c.Name == _botChannel);

        if (channel == c_channel)
        {
            var messages = await c_channel!.GetMessagesAsync(2).FlattenAsync();
            var messageArray = messages.ToArray();

            if (messageArray.Length < 2)
                return;

            switch (messageArray[0].Content)
            {
                case "z":
                    if (messageArray[1].Content == "z")
                        await BrokenChain(c_channel, message);
                    break;
                case "0":
                    if (messageArray[1].Content != "z")
                        await BrokenChain(c_channel, message);
                    break;
                case "r":
                    if (messageArray[1].Content != "0")
                        await BrokenChain(c_channel, message);
                    break;
                default:
                    await BrokenChain(c_channel, message);
                    break;
            }

        }
    }

    private async Task BrokenChain(ISocketMessageChannel channel, SocketMessage message)
    {
        var UNick = ((message.Author as IGuildUser)?.Nickname ?? (message.Author as IGuildUser)?.Username);
        var selectedMessage = string.Format(Messages.MessageList[_random.Next(Messages.MessageList.Length)], UNick);

        try
        {
            await channel.SendMessageAsync(selectedMessage);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error has occured: {ex.Message}");
        }
    }
}