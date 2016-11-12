package com.avatify.alexaavatify;

import com.amazon.speech.slu.Intent;
import com.amazon.speech.speechlet.*;
import com.amazon.speech.ui.PlainTextOutputSpeech;
import com.amazon.speech.ui.Reprompt;
import com.amazon.speech.ui.SsmlOutputSpeech;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

import org.json.*;

public class AvatifySpeechlet implements Speechlet {

    @Override
    public void onSessionStarted(SessionStartedRequest sessionStartedRequest, Session session) throws SpeechletException {
    }

    @Override
    public void onSessionEnded(SessionEndedRequest sessionEndedRequest, Session session) throws SpeechletException {
    }

    @Override
    public SpeechletResponse onLaunch(LaunchRequest launchRequest, Session session) throws SpeechletException {
        try {
            return getCurrentMoodResponse();
        } catch (Exception e) {
            return getErrorResponse();
        }
    }

    @Override
    public SpeechletResponse onIntent(IntentRequest intentRequest, Session session) throws SpeechletException {
        Intent intent = intentRequest.getIntent();
        String intentName = (intent != null) ? intent.getName() : null;

        if ("GetMoodIntent".equals(intentName)) {
            try {
                return getCurrentMoodResponse();
            } catch (Exception e) {
                return getErrorResponse();
            }
        } else if ("AMAZON.StopIntent".equals(intentName)) {
            return getStopResponse();
        } else if ("AMAZON.CancelIntent".equals(intentName)) {
            return getStopResponse();
        } else if ("AMAZON.HelpIntent".equals(intentName)) {
            return getHelpResponse();
        } else {
            return getRepromptResponse();
        }
    }

    private SpeechletResponse getCurrentMoodResponse() throws IOException, JSONException {
        // Request
        String reqUrl = "http://avatify.westeurope.cloudapp.azure.com:8000/api/v1/update/alexa";
        URL url = new URL(reqUrl);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");

        // Response
        InputStream is = connection.getInputStream();
        BufferedReader rd = new BufferedReader(new InputStreamReader(is));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = rd.readLine()) != null) {
            sb.append(line);
        }
        rd.close();

        // Parse JSON
        String jsonStr = sb.toString();
        JSONObject json = new JSONObject(jsonStr);
        /*
        JSONArray tasks = json.getJSONArray("tasks");
        JSONObject currentTask = (JSONObject) tasks.get(0);
        JSONObject mood = (JSONObject) json.getJSONObject("mood");
        String moodStr = mood.getString("feeling");
        Float moodVal = BigDecimal.valueOf(mood.getDouble("value")).floatValue();
        */
        JSONArray dialogs = json.getJSONArray("dialogs");
        String dialog = dialogs.getString(0);

        PlainTextOutputSpeech response = new PlainTextOutputSpeech();
        response.setText(dialog);
        return SpeechletResponse.newTellResponse(response);
    }

    private SpeechletResponse getErrorResponse() {
        String text = "Oops. Something went wrong.";

        PlainTextOutputSpeech response = new PlainTextOutputSpeech();
        response.setText(text);
        return SpeechletResponse.newTellResponse(response);
    }

    private SpeechletResponse getRepromptResponse() {
        PlainTextOutputSpeech response = new PlainTextOutputSpeech();
        response.setText("Could you repeat that?");

        Reprompt reprompt = new Reprompt();
        reprompt.setOutputSpeech(response);

        return SpeechletResponse.newAskResponse(response, reprompt);
    }

    private SpeechletResponse getStopResponse() {
        PlainTextOutputSpeech response = new PlainTextOutputSpeech();
        response.setText("Okay, bye.");
        return SpeechletResponse.newTellResponse(response);
    }

    private SpeechletResponse getHelpResponse() {
        PlainTextOutputSpeech response = new PlainTextOutputSpeech();
        response.setText("");

        Reprompt reprompt = new Reprompt();
        reprompt.setOutputSpeech(response);

        return SpeechletResponse.newAskResponse(response, reprompt);
    }

}
