package com.avatify.azurerpiclient;

import java.io.IOException;
import java.net.URISyntaxException;
import com.microsoft.azure.iothub.DeviceClient;
import com.microsoft.azure.iothub.IotHubClientProtocol;
import com.microsoft.azure.iothub.Message;
import com.microsoft.azure.iothub.IotHubStatusCode;
import com.microsoft.azure.iothub.IotHubEventCallback;
import com.microsoft.azure.iothub.IotHubMessageResult;
import com.google.gson.Gson;
import java.io.IOException;
import java.net.URISyntaxException;
import java.util.Random;
import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;
import java.io.IOException;
import java.net.URISyntaxException;
import org.json.*;

public class App
{
    private static String connString = "DeviceId=rpi_lime;HostName=AvatifyIoT.azure-devices.net;SharedAccessKey=yPsA9YeN/7XKvfTncXWhRw==";
    private static IotHubClientProtocol protocol = IotHubClientProtocol.AMQPS;
    private static String deviceId = "rpi_lime";
    private static DeviceClient client;

    public static void main(String[] args) throws IOException, URISyntaxException, Exception
    {
        client = new DeviceClient(connString, protocol);

        MessageCallback callback = new MessageCallback();
        client.setMessageCallback(callback, null);
        client.open();
        System.out.println("Ready.");
    }

    private static class MessageCallback implements com.microsoft.azure.iothub.MessageCallback {
        public IotHubMessageResult execute(Message msg, Object context) {
            String message = new String(msg.getBytes(), Message.DEFAULT_IOTHUB_MESSAGE_CHARSET);
            System.out.println(message);

            try {
                JSONObject json = new JSONObject(message);
                JSONArray tasks = json.getJSONArray("tasks");

                if (tasks.length() == 0) {
                    Runtime rt = Runtime.getRuntime();
                    Process pr = rt.exec(new String[]{"bash","-c","omxplayer ~/rocky.mp3"});
                }
            } catch (Exception e) {
                // Error? Do nothing
            }

            return IotHubMessageResult.COMPLETE;
        }
    }
}
