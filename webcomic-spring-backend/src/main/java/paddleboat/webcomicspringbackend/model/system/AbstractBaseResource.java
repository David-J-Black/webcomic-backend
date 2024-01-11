package paddleboat.webcomicspringbackend.model.system;

import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;

import java.time.Instant;

public class AbstractBaseResource {

    public AbstractBaseResource() {
        ServiceContext ctx = ServiceContext.getContext();
        ctx.setStartTime(Instant.now());
    }

    protected ResponseEntity<Void> success() {

        ServiceContext ctx = ServiceContext.getContext();

        return ResponseEntity
                .ok()
                .headers(buildResponseHeaders(null))
                .body(null);

    }

    protected <T> ResponseEntity<T> success(T response) {
        ServiceContext ctx = ServiceContext.getContext();

        return ResponseEntity
                .ok()
                .headers(buildResponseHeaders(response))
                .body(response);
    }

    private <T> HttpHeaders buildResponseHeaders(T response) {
        ServiceContext ctx = ServiceContext.getContext();
        ctx.endServiceCall();

        HttpHeaders headers = new HttpHeaders();

        headers.add("executionId", ctx.getExecutionId());
        headers.add("executionStartTime", ctx.getStartTime().toString());
        headers.add("executionEndTime", ctx.getEndTime().toString());

        if (response instanceof byte[]) {
            headers.setContentType(MediaType.IMAGE_PNG);
        }

        return headers;
    }

}
