package paddleboat.webcomicspringbackend.model.system;

import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

/*
 * If I want to define our own standard Exception class, we can make a second function
 * @param e
 * @return
 */
@Slf4j
@ControllerAdvice
public class ComicExceptionHandler {

    /**
     * Handles unhandled exceptions and returns an HTTP response with an error message.
     *
     * @param e the exception that was thrown
     * @return a ResponseEntity containing an ErrorResponse object
     */
    @ExceptionHandler
    public ResponseEntity<ErrorResponse> unhandledException(Exception e) {
        log.error("Unhandled Exception! 🤯", e);

        ServiceContext ctx = ServiceContext.getContext();
        ctx.endServiceCall();
        return ResponseEntity
                .status(HttpStatus.INTERNAL_SERVER_ERROR)
                .headers(buildResponseHeaders())
                .body(new ErrorResponse(e));
    }

    /**
     * Builds the response headers for the service call.
     *
     * @return the HttpHeaders object containing the response headers
     */
    private HttpHeaders buildResponseHeaders() {
        ServiceContext ctx = ServiceContext.getContext();
        ctx.endServiceCall();
        HttpHeaders headers = new HttpHeaders();
        headers.add("executionId", ctx.getExecutionId());
        headers.add("executionStartTime", ctx.getStartTime().toString());
        headers.add("executionEndTime", ctx.getEndTime().toString());
        return headers;
    }
}
