package paddleboat.webcomicspringbackend.model.system;

import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * Http response if we run into an uh oh. A fucky wucky if you may
 */
@Data
@NoArgsConstructor
public class ErrorResponse {
    private String message;

    public ErrorResponse(Exception e) {
        ErrorResponse response = new ErrorResponse();
        response.setMessage(e.getMessage());
    }
}
