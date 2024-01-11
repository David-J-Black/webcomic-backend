package paddleboat.webcomicspringbackend.model;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class PageIndex {
    Integer chapterNumber;
    Integer pageNumber;
}
