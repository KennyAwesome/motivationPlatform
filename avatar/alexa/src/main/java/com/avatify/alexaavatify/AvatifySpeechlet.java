package com.avatify.alexaavatify;

import com.amazon.speech.slu.Intent;
import com.amazon.speech.speechlet.*;
import com.amazon.speech.ui.PlainTextOutputSpeech;
import com.amazon.speech.ui.Reprompt;
import com.amazon.speech.ui.SsmlOutputSpeech;

public class AvatifySpeechlet implements Speechlet {

    @Override
    public void onSessionStarted(SessionStartedRequest sessionStartedRequest, Session session) throws SpeechletException {
    }

    @Override
    public void onSessionEnded(SessionEndedRequest sessionEndedRequest, Session session) throws SpeechletException {
    }

    @Override
    public SpeechletResponse onLaunch(LaunchRequest launchRequest, Session session) throws SpeechletException {
        return getCurrentMoodResponse();
    }

    @Override
    public SpeechletResponse onIntent(IntentRequest intentRequest, Session session) throws SpeechletException {
        Intent intent = intentRequest.getIntent();
        String intentName = (intent != null) ? intent.getName() : null;

        if ("GetMoodIntent".equals(intentName)) {
            return getCurrentMoodResponse();
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

    private SpeechletResponse getCurrentMoodResponse() {
        String text = "You're doing great. Keep it up.";

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
