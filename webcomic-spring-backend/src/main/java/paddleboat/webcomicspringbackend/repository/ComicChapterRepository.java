package paddleboat.webcomicspringbackend.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;
import paddleboat.webcomicspringbackend.model.entitiy.ComicChapter;

import java.util.List;

@Repository
public interface ComicChapterRepository extends JpaRepository<ComicChapter, Long> {

    @Query(value = "select * from comic_chapter where status = 'A'", nativeQuery = true)
    List<ComicChapter> findByStatusCd(String statusCd);
}
