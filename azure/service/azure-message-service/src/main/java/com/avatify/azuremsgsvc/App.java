package com.avatify.azuremsgsvc;

import com.microsoft.azure.iot.service.sdk.*;
import java.io.IOException;
import java.net.URISyntaxException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class App
{
    private static final String connectionString = "HostName=AvatifyIoT.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=fhlXUdidMDXwR06k+DM5qBDzO4CS8DM2hcPtDsw2y/U=";
    private static final String deviceId = "rpi_lime";
    private static final IotHubServiceClientProtocol protocol = IotHubServiceClientProtocol.AMQPS;
    private ServiceClient serviceClient;

    public static void main(String[] args) throws IOException, URISyntaxException, Exception {
        App app = new App();
        app.onStart();

        System.out.println("Ready");

        BufferedReader bufferRead = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String s = bufferRead.readLine();
            System.out.println("Input received: " + s);

            if (s.equals("exit"))
                break;

            app.sendMessage(s);
            System.out.println("Message sent");
        }

        app.onShutdown();

        System.exit(0);
    }

    private void onStart() throws IOException, URISyntaxException, Exception {
        serviceClient = ServiceClient.createFromConnectionString(connectionString, protocol);

        if (serviceClient == null)
            throw new IOException();

        serviceClient.open();
    }

    private void onShutdown() throws IOException, URISyntaxException, Exception {
        serviceClient.close();
    }

    private void sendMessage(String messageStr) throws IOException, URISyntaxException, Exception {

        FeedbackReceiver feedbackReceiver = serviceClient.getFeedbackReceiver(deviceId);
        if (feedbackReceiver != null)
        feedbackReceiver.open();

        Message messageToSend = new Message(messageStr);
        messageToSend.setDeliveryAcknowledgement(DeliveryAcknowledgement.Full);

        serviceClient.send(deviceId, messageToSend);
        System.out.println("Message sent to device");

        FeedbackBatch feedbackBatch = feedbackReceiver.receive(10000);
        if (feedbackBatch != null) {
            System.out.println("Message feedback received, feedback time: "
            + feedbackBatch.getEnqueuedTimeUtc().toString());
        }

        if (feedbackReceiver != null)
        feedbackReceiver.close();
    }
}
